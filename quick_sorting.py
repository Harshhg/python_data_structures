def quick_sort(low,high,ar):
     if(low<high):
          j=partition(low,high,ar)
          quick_sort(low,j,ar)
          quick_sort(j+1,high,ar)

def partition(low,high,ar):
     pivot=ar[low]
     i=low
     j=high
     while(i<j):
          while(ar[i]<=pivot and i<high):
               i+=1
          while(ar[j]>=pivot and j>low):
               j-=1
          if(i<j):
               ar[i],ar[j]=ar[j],ar[i]
     ar[j],ar[low]=ar[low],ar[j]
     return j

ar=[101,5,31,7,9,10,4,7,1,6]
low=0
high=len(ar)-1
print("Before Sorting :",ar)
quick_sort(low,high,ar)
print("After Sorting :",ar)
