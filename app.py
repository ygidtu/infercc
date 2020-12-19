#!/usr/bin/env python3
# -*- coding-utf-8 -*-
u"""
Created at 2020.12.16

4 days to go

Just make it easy

1. form to upload file and record mail
2. email server
3. APIs
    - run
    - upload file
    - provide file
4. a docker image
5. process manager
6. database to record tasks
"""


import hashlib
import math
import os
import time

from typing import List, Optional

import pandas as pd

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import and_
from starlette.responses import FileResponse

import config
import db
import models


__dir__ = os.path.abspath(os.path.dirname(__file__))


async def not_found_exception_handler(request: Request, exc: Exception):
    return RedirectResponse(url="/#/404")

# docs_url=None,
app = FastAPI(
    redoc_url=None,
    openapi_url=None,
    exception_handlers={404: not_found_exception_handler}
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://127.0.0.1:8081",
    "http://127.0.0.1",
    # "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=os.path.join(__dir__, "dist/")), name="static")
app.mount("/data", StaticFiles(directory=config.Server.data), name="data")
templates = Jinja2Templates(directory=os.path.join(__dir__, "dist"))


async def process_upload_file(file: File, genotype: bool):
    if file.content_type != "text/csv":
        return JSONResponse(status_code=400, content={"message": "only csv file allowed"})

    data = await file.read()
    await file.close()

    if len(data) / 1024 / 1024 > 50:
        return JSONResponse(status_code=400, content={"message": "csv file should smaller than 50MB"})

    m = hashlib.md5()
    m.update(data)
    md5 = m.hexdigest()

    o = os.path.join(config.Server.data, md5)
    os.makedirs(o, exist_ok=True)

    f = os.path.join(o, "data.csv")
    if not os.path.exists(f):
        with open(f, "wb+") as w:
            w.write(data)

    try:
        data = pd.read_csv(f)
        del data
    except Exception:
        if os.path.exists(f):
            os.remove(f)
        return JSONResponse(status_code=400, content={"message": "invalid csv file"})
    
    return {"filename": file.filename, "md5": md5}


@app.on_event("startup")
async def startup():
    await db.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.database.disconnect()


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/support")
async def support(source: str, species: Optional[str]=None):
    if source == "species":
        return JSONResponse(content=config.SPECIES)
    elif source == "software":
        return JSONResponse(content=config.SOFTWARE)
    elif source == "tissue":
        if not species:
            return JSONResponse(status_code=400, content={"message": "which species?"})
        
        return JSONResponse(content=sorted(os.listdir(os.path.join(config.Server.ref, species))))


@app.get("/task")
async def tasks(uuid: str):
    data = await db.get_tasks(uuid)

    if data and len(data) > 0:
        data = data[0]
        
        return models.Task(
            uuid=data[0],
            name=data[1],
            create_time=data[2].strftime("%Y-%m-%d, %H:%M:%S"),
            status=data[3],
            species=data[4],
            tissue=data[5],
            tau=data[6],
            software=data[7],
            note=data[8]
        )
    return JSONResponse(status_code=400, content={"message": "failed to get task"})

# uuid=60900e956fa9dbff3f3c4b8ce0f3d66e&species=human&tissue=AdultLung&software=MuSiC&tau=0.9

@app.get("/create")
async def create_task(
    name: str, species: str, tissue: str, 
    tau: float=0.9, software: str="music", 
):
    uuid = await db.create(
        name=name, 
        species=species, 
        tissue=tissue, 
        tau=tau,
        software=software
    )

    data = await db.get_tasks(uuid)

    if data and len(data) > 0:
        data = data[0]

        data = models.Task(
            uuid=data[0],
            name = data[1],
            create_time=data[2].strftime("%Y-%m-%d, %H:%M:%S"),
            status=data[3],
            species=data[4],
            tissue=data[5],
            tau=data[6],
            software=data[7],
            note=data[8]
        )

        return data
    return JSONResponse(status_code=400, content={"message": "failed to create task"})


@app.get("/file")
async def list_file(name: str, s: Optional[str]=None):
    if not s:
        return sorted(os.listdir(os.path.join(config.Server.data, name)))
    return FileResponse(os.path.join(config.Server.data, name, s))


@app.post("/file")
async def create_upload_file(file: UploadFile = File(...)):
    return  await process_upload_file(file, False)


if __name__ == '__main__':
    pass