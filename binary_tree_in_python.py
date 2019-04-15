class NewNode():
    def __init__(self,data):
        self.key=data
        self.left = None
        self.right= None

    #def insert(temp,key)
def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.key,end=" ")
    inorder(temp.right)

def insert(temp,key):
    q=[]
    q.append(temp)
    while(len(q)):
        temp=q[0]
        q.pop(0)

        if not temp.left:
            temp.left=NewNode(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right=NewNode(key)
            break
        else:
            q.append(temp.right)

root=NewNode(10)
root.left=NewNode(9)
root.right=NewNode(8)
root.left.left=NewNode(7)
"""ALready Created Tree -
                          10
                        9    8
                      7
"""
print("Before Insertion INORDER :")
inorder(root)
print("\nEnter number of elements to insert")
x=int(input())
while(x):
    insert(root,input())
    x-=1
print("Afer Insertion INORDER")
inorder(root)
