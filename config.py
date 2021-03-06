#!/usr/bin/env python3
# -*- coding:utf-8 -*-
u"""
Created at 2020.07.15

Configurations for this data project
"""
import os


__dir__ = os.path.abspath(os.path.dirname(__file__))


class Server:
    host = "0.0.0.0"
    port = 8080
    log_level = "info"
    data = "/mnt/data"
    ref = "/mnt/ref"
    keyfile = "/mnt/cov.key"
    cert = "/mnt/cov.pem"
    reload = False


def __species__(ref):
    if os.path.exists(ref):
        return sorted([x for x in os.listdir(ref) if os.path.isdir(os.path.join(ref, x))])
    return []


DATABASE = os.path.join(__dir__, "infercc.db")
SOFTWARE = ("MuSiC", "dtangle")

SPECIES = __species__(Server.ref)


if __name__ == '__main__':
    pass