# Printing all the paths from root-to-leaf
'''
Creating a tree - 
    
       1
     /   \
    2     3
   / \   / \
  4   5  6   7
     /
    8
 
Answer is : 1-2-4
            1-2-5-8
            1-3-6
            1-3-7
'''
class newnode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printpath(root,q):
    q.append(root)
    if root.left is None and root.right is None:
        print("")
        for x in q:
            print(x.data,end=" ")
        q.pop()
        return
    
    if root.left is not None:
        printpath(root.left,q)
    if root.right is not None:
        printpath(root.right,q)
    q.pop()     
   
   
        
# Creating the tree
root = newnode(1)
root.left = newnode(2)
root.right = newnode(3)
root.left.left = newnode(4)
root.left.right = newnode(5)
root.left.right.left = newnode(8)
root.right.left = newnode(6)
root.right.right = newnode(7)

q=[]
printpath(root,q)
