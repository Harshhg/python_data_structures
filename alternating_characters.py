'''
You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching 
adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
For example, given the string AABAAB , remove an A at positions 0 and 3 o make ABAB in 2 deletions.

Function that takes string as argument and returns minimum number of deletion
'''

def alternatingCharacters(s):
    d=0
    prev="None"
    for x in s:
        if x==prev:
            d+=1
        else:
            prev=x
    return d
