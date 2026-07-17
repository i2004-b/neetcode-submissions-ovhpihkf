# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # Make dummy node
        dummy = ListNode(0, head)
        # Point node to dummy (previous spot)
        groupPrev = dummy

        # Iterate while true
        while True:
            # Find the kth element # Need to put groupPrev in here
            kth = self.get_k(groupPrev, k)

            # Check that k is valid
            if not kth:
                # break
                break

            # Save the beginning of the next group
            groupNext = kth.next

            # Declare to pointers to iterate through LL
            prev, curr = kth.next, groupPrev.next

            # Iterate while curr does not go to next group
            while curr != groupNext:
                # Set temporary for curr.next
                tmp = curr.next
                # Assign curr.next to prev
                curr.next = prev
                # Move prev to curr
                prev = curr
                # Move curr to tmp
                curr = tmp

            # Now, change the marker
            # Save the last spot that was originally at the beginning so groupPrev.next points to it
            last_spot = groupPrev.next
            # Need groupPrev.next to point to kth element
            groupPrev.next = kth
            # Set groupPrev to the last_spot
            groupPrev = last_spot

        return dummy.next




    def get_k(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr