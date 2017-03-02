#! /usr/bin/env python
# encoding=utf-8
"""
@version:??
@author:都真全
@time:2016/11/14 9:19
"""

# fw = open('../../data/find_common_words_filtered','w')
# for l in open('../../data/find_common_words'):
#     temp = l.strip('\n').split('\t')
#     if '车' in temp[1]:
#         pass
#     else:
#         fw.write(l)
# fw.close()

fw1 = open('../../data/final_filter.csv','w')
filtered = []
for l in open('../../data/find_common_words_filtered'):
    temp = l.strip('\n').split('\t')
    temp1 = str(temp[0])+str(temp[2])
    filtered.append(temp1)
i = 0
for l in open('../../data/final.csv'):
    i += 1
    print(i)
    temp = l.strip('\n').split(',')
    print(len(temp))
    temp1 = str(temp[0])+str(temp[1])
    if temp1 in filtered:
        pass
    else:
        fw1.write(l)
print(i)
fw1.close()
