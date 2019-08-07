'''
Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.
       10                       10 ------> NULL
      / \                       /      \
     3   5       =>     3 ------> 5 --------> NULL
    / \     \               /  \           \
   4   1   2          4 --> 1 -----> 2 -------> NULL
 
'''
# The connect function takes the root as parameter, and connect all the nodes at the same level

def connect(root):
    q=[]
    q.append(root)
    
    while len(q):
        current = len(q)
        for i in range(current):
            current_node = q[0]
            if i != current-1:
                current_node.nextRight = q[1]
            
            if current_node.left:
                q.append(current_node.left)
            elif current_node.right:
                q.append(current_node.right)
        q.pop(0)
