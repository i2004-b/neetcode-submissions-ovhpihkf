# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointer technique: T: O(n), S: O(1)
        # Declare dummy node that has an initial value of 0 and points to head
        dummy = ListNode(0, head)

        # Intialize left and right pointers
        left = dummy
        right = head # want right to be n-away from head, so use loop

        while n > 0 and right:
            right = right.next
            n -= 1

        # Iterate while R exists and just increment L and R over 1
        while right:
            left = left.next
            right = right.next

        # Set left.next to left.next.next to ignore the value at n (delete it)
        left.next = left.next.next

        # Return head
        return dummy.next