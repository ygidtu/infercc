#!/usr/bin/env python
# -*- coding:utf-8 -*-
u"""
Create runner
"""
import asyncio
import os
import signal
import sys
import time

from multiprocessing import Process
from subprocess import Popen, PIPE, STDOUT

import click
import uvicorn

import config
import db


__dir__ = os.path.abspath(os.path.dirname(__file__))

scripts = {
    "tsidx": os.path.join(__dir__, "./R/tsidx.R"),
    "dtangle": os.path.join(__dir__, "./R/dtangle.R"),
    "music": os.path.join(__dir__, "./R/music.R")
}


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
SETTINGS = os.path.join(__dir__, "settings.ini")
VERSION = "0.1.0"


@click.command(
    context_settings=CONTEXT_SETTINGS,
    short_help="Build scRNA-seq dataset"
)
@click.option(
    "-i", "--input-file", required=True,
    type=click.Path(exists=True),
    help="Path to input file"
)
@click.option(
    "-m", "--meta", required=True,
    type=click.Path(exists=True),
    help="Path to meta file",
)
@click.option(
    "-o", "--output", required=True,
    type=click.Path(),
    help="Prefix of output directory"
)
@click.option(
    "-c", "--column",
    type=str, required = True, show_default=True,
    help="Which column is the cell type"
)
@click.option(
    "-t", "--tau",
    type=float, default=0.9, show_default=True,
    help="minimum tau value to use"
)
@click.version_option(VERSION, message='Current version %(version)s')
def build(input_file:str, meta:str, output:str, column:str, tau:float):
    u"""
    build scRNA-seq dataset
    """
    os.makedirs(output, exist_ok=True)

    o = None
    try:
        p = Popen(f"Rscript {scripts['tsidx']} -f {input_file} -m {meta} -c {column} -t {tau}", shell=True, stdout=PIPE, stderr=STDOUT)

        o = p.stdout.read()

        with open(os.path.join(output, "build.log"), "wb+") as w:
            w.write(o)
    except Exception as err:
        with open(os.path.join(output, "build.log"), "a+") as w:
            w.write(str(err))

@click.command(
    context_settings=CONTEXT_SETTINGS,
    short_help="Run deconvolution"
)
@click.option(
    "-i", "--input-file", required=True,
    type=click.Path(exists=True),
    help="Path to input file"
)
@click.option(
    "-s", "--scset", required=True,
    type=click.Path(exists=True),
    help="Path to scRNA-seq dataset",
)
@click.option(
    "-m", "--method", required=True,
    type=click.Choice([x.lower() for x in config.SOFTWARE]),
    default="music",
    help="Prefix of output directory"
)
@click.option(
    "-o", "--output", required=True,
    type=click.Path(),
    help="Prefix of output directory"
)
@click.version_option(VERSION, message='Current version %(version)s')
def run(input_file:str, scset: str, output:str, method:str):
    u"""
    run deconvolution
    """
    os.makedirs(output, exist_ok=True)

    try:
        p = Popen(f"Rscript {scripts[method]} -f {input_file} -s {scset} -o {output} {column}", shell=True, stdout=PIPE, stderr=STDOUT)

        o = p.stdout.read()
        with open(os.path.join(output, f"{method}.log"), "wb+") as w:
            w.write(o)
    except Exception as err:
        with open(os.path.join(output, f"{method}.log"), "a+") as w:
            w.write(str(err))


@click.command(
    context_settings=CONTEXT_SETTINGS,
    short_help="Run deconvolution"
)
@click.version_option(VERSION, message='Current version %(version)s')
def server():
    u"""
    start server
    """
    if not os.path.exists(config.Server.data):
        os.makedirs(config.Server.data)

    __data__ = config.Server.data
    __SUPPORT__ = config.SOFTWARE

    async def __backgroud__():
        while True:
            try:
                tasks = await db.get_tasks()

                for task in tasks:
                    _, name, _, _, species, tissue, tau, software, _ = task

                    if software in __SUPPORT__:
                        cmd = f"python {__file__} run -m {software} -i {__data__}/{name}/data.csv -s {species}/{tissue}_{tau} -o {__data__}/{name}"
                        print(cmd)
                    else:
                        await db.update(task[0], db.STATUS.Failed, "unknown software")

                await asyncio.sleep(2)
            except KeyboardInterrupt:
                break

    # loop = asyncio.get_event_loop()
    # loop.create_task(__backgroud__())

    # t = Process(target=loop.run_forever)
    # t.start()

    if os.path.exists(config.Server.keyfile) and os.path.exists(config.Server.cert):
        uvicorn.run(
            "app:app",
            host=config.Server.host,
            port=config.Server.port,
            log_level=config.Server.log_level,
            reload=config.Server.reload,
            ssl_keyfile=config.Server.keyfile,
            ssl_certfile=config.Server.cert
        )
    else:
        uvicorn.run(
            "app:app",
            host=config.Server.host,
            port=config.Server.port,
            log_level=config.Server.log_level,
            reload=config.Server.reload,
        )



@click.group(
    context_settings=CONTEXT_SETTINGS,
    invoke_without_command=False
)
@click.version_option(VERSION, message="Current version %(version)s")
def cli():
    u"""
    Welcome
    \f
    Created by Zhang yiming at 2018.11.14
    """
    pass


if __name__ == '__main__':
    cli.add_command(build)
    cli.add_command(run)
    cli.add_command(server)
    cli()

