'''Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?'''
from typing import Optional

from Coding_Skills.LeetCode_21_mergesortedlist import ListNode

# recursive approach
'''
if not head or not head.next:
    return head
reversed_head = self.reverseList(head.next)
head.next.next = head
head.next = None
return reversed_head'''


# iterative approach
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    if head!=None and head.next==None:
        return head
    else:
        temp =  None
        next_node = None
        while head!=None:
            next_node = head.next
            head.next = temp
            temp = head
            head = next_node
    return temp