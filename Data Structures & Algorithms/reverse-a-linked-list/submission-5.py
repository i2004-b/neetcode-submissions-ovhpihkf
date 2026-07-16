# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check that the head exists
        if not head:
            return None

        # Assign a pointer to the head
        # This is needed to hold onto the reversed list at that point
        newHead = head

        # Check that the next element exists
        if head.next:
            # Enter a recursive call to get the reversed section
            newHead = self.reverseList(head.next)
            head.next.next = head

        # Set head.next to None
        head.next = None

        # Return the new head
        return newHead