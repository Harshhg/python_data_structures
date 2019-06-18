# A simple recursive solution to find the height of the tree.
# The function height() takes the root of the tree as parameter.

def height(root):
      if(root is None):
        return 0
    else:
        return 1+max(height(root.left),height(root.right))
    
