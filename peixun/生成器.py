# -*- coding:utf-8 -*-
__author__ = '朱永刚'

"""
杨辉三角
"""

def yangHui(max):
    l = [1]
    i = 0
    while i < max:
        yield l
        l = [1] + [l[temp] + l[temp+1] for temp in range(len(l)-1)] + [1]
        i += 1

for i in yangHui(10):
    print(i)