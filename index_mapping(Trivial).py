# Example of hashing - Index mapping with negative values. (also called Trivial Hashing)

def search(x):
    if x>=0:    # If element is positive
        if (has[x][0])==1:
            return True
        else:
            return False
    
    else:       # If element is negative
        if has[abs(x)][1] == 1:
            return True
        else:
            return False
            
def insert(ar):
    for i in range(len(ar)):
        if ar[i]>=0:
            has[ar[i]][0] = 1
        elif ar[i]<0:
            has[ abs(ar[i]) ][1] = 1


ar = [-1,2,4,-6,5,3]
max = 1000
# Initializing the hash table with 0
has = [[0 for i in range(2)]    for j in range(max + 1)]
# Calling insert function to insert into hash table
insert(ar)
# Searching the value in hash table
result = search(-6)
if result:
    print("Present")
else:
    print("Not present")
