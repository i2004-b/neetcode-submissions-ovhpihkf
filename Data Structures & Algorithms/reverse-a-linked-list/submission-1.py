# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If no head
        if not head:
            return None

        # Variable to return later after reversing list
        # For now, set equal to original head
        newHead = head

        # If head.next is NOT None
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        # Original head now points to None
        head.next = None

        return newHead