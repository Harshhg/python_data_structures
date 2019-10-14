#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 0-1 Knapsack Problem using Dynamic Programming.
# Using Tabulation Method (Filling table in Bottom-up manner)
# Time Complexity is O(nW)


# In[32]:


def knapsack(maxW, weight, val, items):
    # Initializing the table[][] with 0s
    table=[ [0 for x in range(maxW+1)] for x in range(items+1) ] 
    
    # ci = current Item
    # cw = current Weight
    for ci in range(items+1):
        for cw in range(maxW+1):
            
            if ci ==0 or cw == 0:  # Filling 1st row and column with 0
                table[ci][cw]=0
                
            elif weight[ci-1] <= cw:  # if the current weight can be included in the bag capacity
                val_CI = val[ci-1]                        # Value of Current Item
                val_RW = cw - weight[ci-1]                # Max Value of Remaining weight from the current weight
                including = val_CI + table[ci-1][val_RW]  # Including current item
                notIncluding = table[ci-1][cw]            # Not Including current item
                
                table[ci][cw] = max(including, notIncluding)
                
                # --------------  OR IN 1 LINE --------------#
                
                # table[ci][cw] = max(val[ci-1] + table[ci-1][cw-weight[ci-1]]   ,  table[ci-1][cw])
                
            else:
                table[ci][cw]= table[ci-1][cw]       
                
    # The last value in the table is our final answer
    print("Answer is : " , table[ci][cw])
    # Printing the table for reference
    print("\n",table)


# In[33]:


val = [60,100,120]
weight = [10,20,30]
maxW = 50
items = len(val)
knapsack(maxW, weight, val, items)


# In[ ]:


# stay Tuned :)

