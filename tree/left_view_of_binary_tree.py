#  Prints the Left view of the Binary Tree
# Function printLeftView takes the root of the tree as input and print the left view of the binary tree

def traversetree(root,ml,level):
    if(level>ml):
        print(root.data,end=" ")
        ml=level
    if(root.left is not None):
        ml =visittree(root.left,ml,level+1)
    if(root.right is not None):
        ml = visittree(root.right,ml,level+1)
    return ml
    
    
    
def printLeftView(root):
    traversetree(root,0,1)
   
