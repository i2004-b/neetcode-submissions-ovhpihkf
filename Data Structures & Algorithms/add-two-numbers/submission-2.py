# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Optimized Way: T:O(m + n), S: O(1)
        # Main trick: keep track of the carry digit; no need to reverse the list or the numbers to add the numbers

        # Declare a dummy node and also a curr pointer
        curr = dummy = ListNode()

        # Initialize a carry value
        carry = 0

        # Iterate while the at least 1 list is non-empty or while the carry digit exists
        while l1 or l2 or carry:
            # Get the values of l1 and l2 if they exist (otherwise set to 0 in order to add)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Get the total value of adding v1, v2, and carry
            val = v1 + v2 + carry

            # Get the new carry digit by flooring by 10
            carry = val // 10
            # Get the value to put in the new node by modding by 10
            val = val % 10

            # Set the next node to the val
            curr.next = ListNode(val)

            # Update pointer
            curr = curr.next
            # Update like this to ensure that the pointer keeps moving as long as it is not Null
            # Do this so that there are no errors when going to the next item when None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
