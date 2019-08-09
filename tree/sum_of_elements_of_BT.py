# Recursive solution to find the sum of all elements of binary tree.
'''
Creating a tree - 
    
       1
     /   \
    2     3
   / \   / \
  4   5  6   7
     /
    8
 
Answer is : 36
'''
class newnode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def add(root):
    if not root:
        return 0
    return root.data + add(root.left) + add(root.right)

# Creating the tree
root = newnode(1)
root.left = newnode(2)
root.right = newnode(3)
root.left.left = newnode(4)
root.left.right = newnode(5)
root.left.right.left = newnode(8)
root.right.left = newnode(6)
root.right.right = newnode(7)

print(add(root))
