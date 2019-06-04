#   Function that takes head of a linked list and return true is the linked list contains cycle otherwise false
#   1-True  0 -False

def has_cycle(head):
    slow=head
    fast=head.next
    while(1):
        if(slow.next is None or fast.next is None or fast.next.next is None):
            break
        else:
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return 1
    return 0
