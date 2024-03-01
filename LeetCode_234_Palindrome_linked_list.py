'''234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9



Follow up: Could you do it in O(n) time and O(1) space?'''
from typing import Optional

from Coding_Skills.LeetCode_21_mergesortedlist import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
           return True
        elif head != None and head.next == None:
             return True
        else:
            fast = head
            slow = head
            stack = []
            while fast != None and fast.next != None:
                  stack.append(slow.val)
                  slow = slow.next
                  fast = fast.next.next
                  #madam
            if fast != None:
                     slow = slow.next
            while slow != None:
                if slow.val != stack.pop():
                   return False
                else:
                   slow = slow.next
            return True
