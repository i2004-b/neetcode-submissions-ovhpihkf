# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.N = n

        def rec(head):
            # Base case: if the head does not exist return None
            if not head:
                return None

            # Set head.next to the function call (recursion)
            head.next = rec(head.next)

            # Decrement n, which happens on the way back up from the list
            self.N -= 1

            # Check if you need to delete node or not
            if self.N == 0:
                return head.next
            else:
                return head
        
        # Call function
        return rec(head)