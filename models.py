#!/usr/bin/env python3
# -*- coding:utf-8 -*-
u"""
Created at 2020.12.17

FastAPI models
"""
from typing import List, Optional

from pydantic import BaseModel


class Task(BaseModel):
    uuid: str
    name: str
    create_time: str
    status: str
    species: str
    tissue: str
    tau: float
    software: str
    note: str
