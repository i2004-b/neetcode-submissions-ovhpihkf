# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Pointers both start at the same time at the head
        s, f = head, head

        # Iterate while f exists and f.next exists in order to jump by 2
        # If the while condition iterates to false, no cycle
        while f and f.next:
            # Advance s by 1
            s = s.next
            # Advance f by 2
            f = f.next.next
            # If both end up at the same point, return True
            if s == f:
                return True

        # No cycle, return False
        return False
