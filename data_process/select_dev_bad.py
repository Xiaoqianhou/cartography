#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
s0 = list(open(r'/home/gdmlab/qxh/mary/0421/333/333/cartography-main/filtered/cartography_confidence_0.01/QNLI/train.tsv').readlines())
f = open(r'intersection.tsv','w',newline = '')
writer = csv.writer(f,delimiter='\t')
for i in s0:
    i = i.split('\t')
    if i[0] == 'index' or int(i[0]) >= 104743:
        writer.writerow(i)

