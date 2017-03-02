#! /usr/bin/env python
# encoding=utf-8
"""
@version:??
@author:都真全
@time:2016/11/13 15:13
"""
from __init__ import *

fw  = open('../../data/find_common_words','w')

common_views = []
a = datetime.now()
print(a)
for l in open('../../data/common_words'):
    temp = l.strip('\n')
    common_views.append(temp)
for l in open('result3.csv'):
    temp = l.strip('\n').split('\t')
    if temp[2] in common_views:
        fw.write(l)
fw.close()
b = datetime.now()
print(b)
print((b-a).seconds)

