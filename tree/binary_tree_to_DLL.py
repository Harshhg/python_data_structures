# Here the function bToDLL(root) would take root of tree as parameter and must return the head of the doubly linked list.
'''
           10
          /  \
         20   30
        /  \
       40   60

So, DLL would be 40<=>20<=>60<=>10<=>30.
'''

def convertToDLL(root,prev):
    if root is None:
        return prev
    
    prev = dll(root.left, prev)
    
    if prev:
        root.left = prev
        prev.right = root
    prev =root   
  
    prev = dll(root.right,prev)
    return prev
    
    
def bToDLL(root):
    head = convertToDLL(root,None)
    while(head.left):
        head = head.left
    return head
