#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Find the length of the longest consecutive subsequence in array.
# Consecutive sequence can be in any order.

'''
Input:
2
7
2 6 1 9 4 5 3
7
1 9 3 10 4 20 2

Output:
6      (1,2,3,4,5,6)
4      (1,2,3,4)
'''


# In[2]:


ar=[2,6,7,1,9,4,5,3]


# In[6]:


# Creating hash table and mapping values.
hash={}
for x in ar:
    if x not in hash:
        hash[x]=1


# In[4]:


maxcount=0
count=0
for x in ar:
    count=0
    if x-1 in hash:
        count+=1 
    temp=x
    while(temp in hash):
        count+=1
        temp+=1
    maxcount= max(maxcount,count)


# In[5]:


print(maxcount)


# In[ ]:


# stay Tuned :)

