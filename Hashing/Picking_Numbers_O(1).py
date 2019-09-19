#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Given an array of integers, find and print the maximum number of integers you can select from the array such that 
the absolute difference between any two of the chosen integers is less than or equal to 1

For ex -  [6,2,1,3,3,5]
elements with abs difference < 1 are -  [2,3,3]
so the output is 3.

For ex - [1 2 2 3 1 2]
elements with abs difference < 1 are -  [1,1,2,2,2]
so the output is 5.

'''
# Time complexity - O(1) using HASHING
    


# In[4]:


ar = list(map(int, input().rstrip().split()))
hash=[0]*1000
for x in ar:
    hash[x]+=1
    
res=0
for x in range(1000):
    res=max(res,hash[x-1]+hash[x])
    
print(res)


# In[47]:


# O(N) solution is in the array section.
# stay Tuned :)

