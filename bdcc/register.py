# -*- coding: utf-8 -*-

import os.path as osp
import json
import argparse
from getpass import getpass
import requests

from utils import use_logging, write_log, finish_logging

if __name__ == "__main__":

    droot = osp.dirname(__file__)

    use_logging("bluedragonclub-logging",
                mode='a',
                fout=True,
                fpath=osp.join(droot, "log.txt"))


    try:

        student = {
            "id": "20041052",
            "pw": "asdf@asdf",
            "name": "이대원",
            "group": 1 
        }

        url = "http://localhost:8000/register"

        response = requests.post(url=url, json=student)

        res = response.json()

        write_log("\n{}".format(res))
    finally:
        finish_logging()
