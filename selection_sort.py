def selection_sort(ar):
     for i in range(0,len(ar)):
          min=i          #Stroing index value only
          for j in range(i,len(ar)):
               if(ar[j]<ar[min]):  #Comparing  value at index
                    min=j
          ar[i],ar[min]=ar[min],ar[i]   #Swapping index values

ar=[2,4,17,1,9,3]
print("Before Sorting : ",ar)
selection_sort(ar)
print("After Sorting: ",ar)
