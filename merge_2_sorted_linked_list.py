#Continuing from the function that takes head pointer of both sorted linked list and return head of merged sorted linked list.

def mergeLists(head1, head2):
    current=head1
    previous=head1
    while(current is not None and head2 is not None):
        if(head1.data>=head2.data and current.data==previous.data):
            previous=head2
            head2=head2.next
            previous.next=head1
            head1=previous
        elif(current.data>=head2.data):
                previous.next=head2
                head2=head2.next
                previous.next.next=current
                previous=previous.next
        else:
            previous=current
            current=current.next
    if head2 is not None :
        previous.next=head2    
    return head1
