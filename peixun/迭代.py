# -*- coding:utf-8 -*-
__author__ = '朱永刚'
"""
使用迭代查找一个list中最小和最大值，并返回一个tuple：
"""

l = list(range(10))
max = l[0]
min = l[0]

for i in l:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min,max)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a + b
        n += 1

fib(4)