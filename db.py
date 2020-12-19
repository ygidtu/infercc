#!/usr/bin/env python3
# -*- coding: utf-8-*-
u"""
Created at 2020.12.16

Try to use sqlalchemy to add a simple task backend
"""
import os
import datetime
import uuid

import databases
import sqlalchemy

from sqlalchemy import and_

import config


class STATUS:
    Created="Created"
    Running="Runing"
    Finished="Finished"
    Failed="Failed"


# SQLAlchemy specific code, as with any other app
DATABASE_URL = f"sqlite:///{config.DATABASE}"
print(DATABASE_URL)
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, index=True),
    sqlalchemy.Column("create_time", sqlalchemy.DateTime),
    sqlalchemy.Column("status", sqlalchemy.String, index=True),
    sqlalchemy.Column("species", sqlalchemy.String),
    sqlalchemy.Column("tissue", sqlalchemy.String),
    sqlalchemy.Column("tau", sqlalchemy.Float),
    sqlalchemy.Column("software", sqlalchemy.String),
    sqlalchemy.Column("note", sqlalchemy.String)
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


async def exists(
    name: str, species: str, 
    tissue: str, tau: float, 
    software: str, run_on_server: bool = True
):
    query = tasks.select().where(and_(
        tasks.columns.name == name,
        tasks.columns.species == species, 
        tasks.columns.tissue == tissue,
        tasks.columns.tau == tau,
        tasks.columns.software == software
    ))
    temp = await database.fetch_all(query)
    print(temp)
    if not temp:
        return False
    return temp[0][0]


async def create(
    name: str, species: str, 
    tissue: str, tau: float, 
    software: str, run_on_server: bool = True
):
    if not run_on_server:
        await database.connect()

    e = await exists(name, species, tissue, tau, software)

    if not e:
        uid = str(uuid.uuid4())
        query = tasks.insert().values(
            id=uid,
            name = name,
            create_time=datetime.datetime.now(),
            status=STATUS.Created,
            species=species,
            tissue=tissue,
            software=software,
            tau=tau,
            note="normal"
        )
        await database.execute(query)
    else:
        uid = e

    if not run_on_server:
        await database.disconnect()
    return uid


async def update(uid: str, status: str, note: str, run_on_server: bool = True):
    if not run_on_server:
        await database.connect()

    query = tasks.update().values(
        status=status, note=note
    ).where(tasks.columns.id == uid)
    
    await database.execute(query)

    if not run_on_server:
        await database.disconnect()


async def delete(uid: str, run_on_server: bool = True):
    if not run_on_server:
        await database.connect()

    query = tasks.delete().where(tasks.columns.id == uid)
    await database.execute(query)

    if not run_on_server:
        await database.disconnect()


async def get_tasks(uid: str="", run_on_server: bool = True):
    if not run_on_server:
        await database.connect()
    if not uid:
        query = tasks.select().where(tasks.columns.status == STATUS.Created)
    else:
        query = tasks.select().where(tasks.columns.id == uid)

    data = await database.fetch_all(query)
    if not run_on_server:
        await database.disconnect()

    if data and not os.path.join(config.Server.data, data[0][1]):
        await delete(data[0][0])
    return data


if __name__ == '__main__':
    import asyncio

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    for i in range(10):
        loop.run_until_complete(create(f"{i}", "human", "lung", 0.9, "music"))

    print(loop.run_until_complete(get_tasks()))

    loop.close()