# function that return 1 (TRUE) if a tree is BINARY SEARCH TREE else return 0 (False)
# function isBST takes root as parameter.

def inorder(root,ar):
    if(root):
        ar=inorder(root.left,ar)
        ar.append(root.data)    
        ar=inorder(root.right,ar)
    return ar
    
def isBST(root):
    ar=[]
    ar=inorder(root,ar)
    max=0
    for x in ar:
        if x>max:
            max=x
        else:
            return 0
    return 1
       
