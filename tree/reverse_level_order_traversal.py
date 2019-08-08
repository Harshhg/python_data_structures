# Printing the level order of the tree in reverse order
'''
Creating a tree - 
    
       1
     /   \
    2     3
   / \   / \
  4   5  6   7
  
 
Answer is :  4 5 6 7 2 3 1
'''
class newnode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def reverse(root):
    q=[]
    stack=[]
    q.append(root)
    while(len(q)):
        cur = q[0]
        if cur.right is not None:
            q.append(cur.right)
        if cur.left is not None:
            q.append(cur.left)
        stack.append(cur.data)
        q.pop(0)
    while(len(stack)):
        print(stack.pop())
        
# Creating the tree
root = newnode(1)
root.left = newnode(2)
root.right = newnode(3)
root.left.left = newnode(4)
root.left.right = newnode(5)
root.right.left = newnode(6)
root.right.right = newnode(7)

reverse(root)
