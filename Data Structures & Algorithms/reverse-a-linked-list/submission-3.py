# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: if the head does not exist, return nothing
        if not head:
            return None

        # Set newHead to the current head
        newHead = head

        # If head.next exists, run the recursion
        if head.next:
            # This works in a way which the last node will be the node propagated back through
            newHead = self.reverseList(head.next)
            # Set the head.next.next to head to reverse chain
            head.next.next = head

        # Set head.next to None
        head.next = None
        return newHead