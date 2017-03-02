#! /usr/bin/env python
# encoding=utf-8
"""
@version:??
@author:都真全
@time:2016/11/1 11:35
"""
from __init__ import *
def delete(matchs):
    l = len(matchs)
    matchs.sort(key=lambda x: len(x))
    change = []
    for m in range(0, l):
        for n in range(m + 1, l):
            if matchs[m] in matchs[n]:
                if matchs[m] not in change:
                    change.append(matchs[m])
    if len(change):
        for c in change:
            matchs.remove(c)
    return matchs
def get_view_result(test,views,fw):
    for i in range(0,len(test)):
        SentenceId = test.loc[i,'SentenceId']
        Content1 = test.loc[i,'Content']
        # conlen = len(Content1)
        # Content = ''.join('%s' % Content1).decode('utf-8')
        # tags = 'pos'
        matchs = []
        for j in range(0,len(views)):
            pattern = re.compile(str(views[j]))
            match = pattern.findall(Content1)
            if len(match) != 0 and match[0] not in matchs:
                matchs.append(match[0])
        if len(matchs)!=0:
            if len(matchs) >0:
                matchs = delete(matchs)
            for m in matchs:
                # fw.write(str(i)+'\t')
                fw.write(str(SentenceId) + '\t')
                fw.write(Content1+'\t')
                fw.write(m+'\t')
                # fw.write(tags+'\t')
                # fw.write(str(conlen))
                fw.write('\n')
        if i%100 == 0:
            print (str(i)+":"),
    fw.close()
views = []
for l in open("views.csv"):
    temp = l.strip('\n')
    views.append(temp)
fw = open('result1.csv','w')
# fw1 = open('../data/id_views.csv','w')
print(len(views))
try:
    test = pd.read_csv('test_split1.csv',sep=',')
    get_view_result(test, views, fw)
except Exception,e:
    print(str(e))







