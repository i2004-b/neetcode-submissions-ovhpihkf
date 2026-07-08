# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two Pass Solution: T: O(n), S: O(1)

        # Part 1: Get length of list
        length = 0
        # Set curr to head
        curr = head
        # Iterate while curr exists
        while curr:
            length += 1
            curr = curr.next

        # Part 2: Figure out the "index" to remove at
        remove = length - n # Ensures it works with the 0-indexing of a loop

        # Part 3: Check that remove is 0, if it is, just return head.next
        if remove == 0:
            return head.next

        # Part 4: Iterate through the list length - 1. At every element, check if the next element is the one to remove
        # Set curr to head again
        curr = head

        for i in range(length - 1):
            if (i + 1) == remove:
                curr.next = curr.next.next
                break

            # Otherwise, increment curr by 1
            curr = curr.next

        # Return head
        return head
        