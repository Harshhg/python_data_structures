# The Shortest Recursive Solution to check whether two trees are identical or not.
# The isIdentical  function takes root pointer of two trees... and return True if identical and False if not.

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.data==root2.data) and (isIdentical(root1.left,root2.left)) and (isIdentical(root1.right,root2.right))
