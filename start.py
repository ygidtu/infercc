#!/usr/bin/env python3
# -*- coding:utf-8 -*-
u"""
Start lab page
"""
import os
import sys
import argparse
from subprocess import check_call

__dir__ = os.path.abspath(os.path.dirname(__file__))
__webname__ = os.path.basename(__dir__)

def main(port=8080, verbose=False, daemon=True):
    port = f"-p {port}:8080" if port is not None else ""
    daemon = "-d" if daemon else ""

    cmd = f"docker run --user $(id -u):$(id -g) --name {__webname__} {port} {daemon} -v {__dir__}:/mnt/ -v {__dir__}/infercc.db:/opt/infercc/infercc.db ygidtu/{__webname__} server"

    if verbose:
        print(cmd)

    check_call(cmd, shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Start das web service.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-d", "--daemon", action="store_true",
        help="whether to run in daemon mode"
    )
    parser.add_argument(
        '-p', '--port',
        help='the port of this web service'
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="print the docker command"
    )

    args = parser.parse_args()
    main(port=args.port, verbose=args.verbose, daemon=args.daemon)
    
