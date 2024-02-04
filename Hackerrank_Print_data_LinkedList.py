'''This is an to practice traversing a linked list. Given a pointer to the head node
of a linked list,
print each node's  element, one per line.
If the head pointer is null (indicating the list is empty),
 there is nothing to print.'''

def printLinkedList(head):
    if head is None:
        print("")
    cur = head
    while (cur):
          print(cur.data)
          cur = cur.next