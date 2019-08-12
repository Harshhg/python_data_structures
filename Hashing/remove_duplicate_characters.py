# Removing Duplicates from the array of characters.. using HASHING
# Used Dictionary for hashing implementation.

ar =  ['a','b','c','a','d','c','e','a','e','k','c']

dict = {}
for x in ar:
    if x not in dict:
        dict[x]=1
    else:
        dict[x] = dict[x]+1
        
new=[]
for x in ar:
    if dict[x] > 0:
        new.append(x)
        dict[x]=0
print("Before Removing Duplicates :",ar)
print("After Removing Duplicates : ",new)
