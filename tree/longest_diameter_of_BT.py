# function diameter takes root of a tree as parameter... and return the longest diameter

def height(node):
    if node is None:
        return 0
    else:
        return 1+max(height(node.left),height(node.right))
        
def diameter(root):
    if root is None:
        return 0
    
    # Height of left and right subtree
    lh = height(root.left)
    rh = height(root.right)

    # Diameter of left and right subtree
    ld = diameter(root.left)    
    rd = diameter(root.right)
    
    # return the maximum of (height of left+right+1 and max diameter)
    return max(lh+rh+1, max(ld,rd))
