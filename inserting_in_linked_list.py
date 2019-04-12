class Node: #Creating Node having data and next pointer
    def __init__(self,data):
        self.data=data
        self.next=None
class Mylist:
    def __init__(self): #For initializing HEAD node
        self.head=None;

    def push(self,new_data):    #To insert data at the end of linked list
        new_node = Node(new_data) #creating a temporary new node
        if(self.head is None):   #if head node is empty
            self.head=new_node   #creating head node
        else:                      # else if head node exist
            temp=self.head          #assigning temp to the head node
            while(temp.next):
                temp=temp.next      #searching for the last node
            temp.next=new_node      #appending new node to the next of previous node

    def print(self):  #To print the Linked List
        while(self.head):
            print(self.head.data)
            self.head=self.head.next

l= Mylist() #Creating object of class, and initialize head node
n=int(input("Enter number of elements :"))
while(n):
    l.push(input())
    n=n-1
l.print()
