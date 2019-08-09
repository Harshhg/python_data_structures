# Recursive solution to convert a tree into its mirror tree
'''
Creating a tree - 
    
       1
     /   \
    2     3
   / \   / \
  4   5  6   7
     /
    8
 
Answer is : 

       1
     /   \
    3     2
   / \   / \
  7   6  5   4
          \
           8
'''
class newnode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.data)
    inorder(temp.right)

def mirror(root):
    if root:
        mirror(root.left)
        mirror(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
    return root
    
# Creating the tree
root = newnode(1)
root.left = newnode(2)
root.right = newnode(3)
root.left.left = newnode(4)
root.left.right = newnode(5)
root.left.right.left = newnode(8)
root.right.left = newnode(6)
root.right.right = newnode(7)

print("Before Mirror : ")
inorder(root)
mirror(root)
print("After Mirror : ")
inorder(root)
