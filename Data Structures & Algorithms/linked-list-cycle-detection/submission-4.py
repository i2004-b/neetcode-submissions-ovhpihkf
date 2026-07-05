# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Slow and fast pointer technique to find a cycle
        # Both start at the head
        s, f = head, head

        # f will reach the end first if there is an end, so iterate while f is true
        # Check that f.next exists as you are adding it by two
        while f and f.next:
            # Increment s by 1 and f by 2
            s = s.next
            f = f.next.next

            # Check if the are equal
            if s == f:
                return True

        return False
