#   Function that takes head of a linked list and return true is the linked list contains cycle otherwise false



def has_cycle(head):
    flag=0
    singlejump=head
    doublejump=head.next
    while(1):
        if(singlejump.next is None or doublejump.next is None or doublejump.next.next is None):
            break
        else:
            singlejump=singlejump.next
            doublejump=doublejump.next.next
            if(singlejump==doublejump):
                flag=1
                break
    if(flag==1):
        return True
    else:
        return False
