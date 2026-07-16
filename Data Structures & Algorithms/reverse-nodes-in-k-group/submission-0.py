# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check that the head exists
        if not head:
            return None

        # Make a dummy pointer
        dummy = ListNode(0, head)
        # Make a pointer that will point to the end of the previous section
        groupPrev = dummy

        # Iterate while true
        while True:
            # Get the kth element through a helper function
            kth = self.get_k(groupPrev, k)

            # Check that the kth item is valid
            if not kth:
                break

            # Keep track of the node for the beginning of the next section
            groupNext = kth.next

            # Set previous and current pointers to point to
            prev, curr = kth.next, groupPrev.next # previous set to the next section and curr to the beginning of the new section

            # Iterate as long as curr does not go to next section
            while curr != groupNext:
                # Save next pointer
                tmp = curr.next
                # Connect curr to prevous; note: the first element will become the end of the segment and point to the next list
                curr.next = prev
                # Move prev to where curr is
                prev = curr
                # Move curr to where tmp is
                curr = tmp

            # Now readjust pointers so that groupPrev goes to the right spot
            # Save the spot groupPrev.next is at as this is the end of the new segment
            tmp = groupPrev.next # This is the end of the new segment
            # Connect previous list to the new list but connecting to kth item which became first
            groupPrev.next = kth
            # Set groupPrev to where tmp is
            groupPrev = tmp
        
        return dummy.next




    def get_k(self, curr, k):
        # Get k by iterating through to get to kth value
        while curr and k > 0:
            curr = curr.next
            k -= 1

        # Return end spot
        return curr