def binary_search(ar,left,right,element):
     if(right>=left):
          mid=int((right-left)/2)+left
          if(ar[mid] == element):
               return mid
          elif(element<ar[mid]):
               return binary_search(ar,left,mid-1,element)
          else:
                return binary_search(ar,mid+1,right,element)
     else:
          return -1
ar=[2,4,5,7,15,17,80,100]
left=0
element=7
result=binary_search(ar,left,len(ar),element)
if(result!=-1):
     print("Element is present at",result)
else:
     print("Element not found")
