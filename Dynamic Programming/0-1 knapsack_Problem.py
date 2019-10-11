#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  0 - 1 Knapsack Problem using Recursion ( Without Dynamic Programming )


# In[19]:


def knapsack(maxW, weight, val, items):
    # if bag capacity becomes full (maxW=0), or we have traversed all items, return 0
    if items ==0  or maxW == 0:
        return 0
    
    # If current item weight is more than bag capacity(maxW), we cannot include that item, so move to next item.
    if maxW < weight[items]:
        return knapsack(maxW, weight, val, items-1)
    
    else:
        including    =  knapsack(maxW-weight[items], weight, val, items - 1)  + val[items]  # Including current item
        notIncluding =  knapsack(maxW, weight, val, items - 1)                              # Not Including current item
        
        return max(including,notIncluding)


# In[21]:


val = [60,100,120]
weight = [10,20,30]
maxW = 50
items = len(val)-1

ans = knapsack(maxW, weight, val, items)
print(ans)


# In[ ]:


# stay Tuned :)

