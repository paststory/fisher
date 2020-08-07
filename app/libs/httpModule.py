# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 12:04
# @Author  : yang
# @File    : httpModule.py
import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        else:
            return r.json() if return_json else r.text