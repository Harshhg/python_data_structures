#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Given two strings, determine if they share the common substring
# Time complexity O(N)


# In[3]:


# Function that takes 2 strings as arguments
def twoStrings(s1, s2):
    hash={}
    string="NO"
    for x in s1:
        hash[x]=1
    for y in s2:
        if y in hash:
            string="YES"
    return string


# In[8]:


s1="HELLO"
s2="WORLD"
print(twoStrings(s1,s2))


# In[ ]:


# stay Tuned :)

