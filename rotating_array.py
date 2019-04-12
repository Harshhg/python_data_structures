a=[1,2,3,4,5,6] #array
d=2 #rotate number of times
b=[0]* len(a) #Defining Blank Array of size 6
for x in range(0,len(a)):
    if d>=len(a):
        d=d-len(a)
    b[x]=a[d]
    d=d+1
print(b)
