# function that insert a node into sorted doubly linked list
# takes the head of the sorted doubly linked list and the new node value..

def sortedInsert(head, data):
    newnode = DoublyLinkedListNode(data)
    temp=head
    pre=temp
    while(temp is not None):
        if (newnode.data<=temp.data and temp.prev is None):
            newnode.prev=None
            newnode.next=temp
            temp.prev=newnode
            head=newnode
            return head
        elif (newnode.data>=temp.data and temp.next is None):
            newnode.prev=temp
            newnode.next=None
            temp.next=newnode
            return head
        elif(newnode.data<=temp.data):
            newnode.prev=pre
            newnode.next=temp
            pre.next=newnode
            temp.prev=newnode
            pre=newnode
            return head
        else:
            pre=temp
            temp=temp.next
