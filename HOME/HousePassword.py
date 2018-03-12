# -*- coding:utf-8 -*-
__author__ = '朱永刚'

import re

def checkio0(data):
    if len(data) < 10:
        return False
    if not re.compile('[A-Z]+').findall(data):
        return False
    if not re.compile('[a-z]+').findall(data):
        return False
    if not re.compile('[0-9]+').findall(data):
        return False
    return True

def checkio(data):
    return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data) >= 10 else False


