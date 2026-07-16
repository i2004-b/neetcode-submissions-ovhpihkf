# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if can be reversed
        if not head:
            return None

        # Set a pointer to newHead (which will holds the reversed list)
        newHead = head

        # Check if head.next exists and if so, enter recursive calls
        if head.next:
            newHead = self.reverseList(head.next)
            # Change the direction of pointers
            head.next.next = head

        # Point head.next to Null
        head.next = None

        # Return newHead
        return newHead