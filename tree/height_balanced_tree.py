# Check if a tree is Height Balanced or NOT.
'''
Creating a tree - 
    
       1
     /   \
    2     3
   / \   
  4   5  
     /
    8
 
Answer is : False
Since, Height of left subtree - Height of Right Subtree > 1 (3-1 = 2)
'''
class newnode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))   # Returns the height of the tree
        
def isBalanced(root):
    if root is None:
        return 0
    return True and (abs(height(root.left) - height(root.right)) <= 1) 
    '''
    True and False = False
    True and True = True
    So if one subtree is not height balanced, then the entire result is FALSE.
    '''

# Creating the tree
root = newnode(1)
root.left = newnode(2)
root.right = newnode(3)
root.left.left = newnode(4)
root.left.right = newnode(5)
root.left.right.left = newnode(8)

print(isBalanced(root))
