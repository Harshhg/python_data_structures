# Shortest Recursive Solution to count leaf nodes in a tree
# This function takes root of tree as a parameter, and returns the number of leaf nodes count.


def countLeaves(root):
    if not(root.left and root.right):
        return 1
    return (countLeaves(root.left) + countLeaves(root.right))
