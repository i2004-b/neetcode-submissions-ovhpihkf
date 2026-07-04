# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Declare a previous pointer
        prev = None

        # Iterate while the LL exists
        while head:
            # Save what head is pointing to
            new = head.next
            # Set head.next to the previous pointer
            head.next = prev
            # Move prev to where head is
            prev = head
            # Set head to new
            head = new

        return prev