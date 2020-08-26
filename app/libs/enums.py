# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 18:03
# @Author  : yang
# @File    : enums.py
from enum import Enum


class PendingStatus(Enum):
    """交易状态"""
    waiting = 1
    success = 2
    reject = 3
    redraw = 4