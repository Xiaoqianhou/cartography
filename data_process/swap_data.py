#!/usr/bin/env python
# coding: utf-8

# In[1]:



import csv
import os
for i in range(21):
    new_fold = 'qnli'+str(i)
    os.mkdir(new_fold)
    fwd = open(new_fold+'/dev.tsv','a',newline = '',encoding = 'utf-8')
    tsv_wd = csv.writer(fwd,delimiter = '\t')
    fwt = open(new_fold+'/train.tsv','a',newline = '',encoding = 'utf-8')
    tsv_wt = csv.writer(fwt,delimiter = '\t')
    with open('train1.tsv','r',newline = '',encoding = 'utf-8') as f:
        j = 0
        tsvreader = csv.reader(f,delimiter = '\t')
        for line in tsvreader:
           # print(j)
           
            if j ==0:
                tsv_wd.writerow(line)
                tsv_wt.writerow(line)
            elif j >= i*5247+1 and j <=i*5247+5247:
                
                tsv_wd.writerow(line)
                
            else:
                tsv_wt.writerow(line)
            j = j+1
           # print(line)
    
    f.close()
    
    fwt.close()


# In[ ]:




