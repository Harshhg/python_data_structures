def bubble_sort(ar):
     l=len(ar)
     for i in range(0,l):
          for j in range(0,l-1):
               if(ar[j]>ar[j+1]):
                    ar[j],ar[j+1]=ar[j+1],ar[j]

ar=[2,4,17,1,9,3]
print("Before Sorting : ",ar)
bubble_sort(ar)

print("After Sorting: ",ar)
 
