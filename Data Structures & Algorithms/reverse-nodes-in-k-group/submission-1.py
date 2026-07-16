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

        # Declare dummy node that points to the head
        dummy = ListNode(0, head)
        # Make a pointer that points to the previous section
        groupPrev = dummy

        # Iterate while true
        while True:
            # First: find the kth element
            kth = self.get_k(groupPrev, k)

            # Check if the kth value is valid
            if not kth:
                break # break if no more to reverse

            # Save the beginning of the next group (for the loop reversal)
            groupNext = kth.next

            # Set previous and curr pointers
            # Prev should begin by pointing at the next group and curr should be at the first element
            prev, curr = kth.next, groupPrev.next
            
            # Iterate while curr does not go on past k
            while curr != groupNext:
                # Save curr.next
                tmp = curr.next
                # Set curr.next to previous
                curr.next = prev
                # Set previous over to curr
                prev = curr
                # Move current over to where it was originally pointing at
                curr = tmp

            # d --> 1 --> 2 --> 3 --> if k =  3 ----> 3 --> 2 --> 1 <- du
            # groupPrev still pointing to 1 when it should be pointing to 3 to 
            tmp = groupPrev.next
            groupPrev.next = kth
            # The item before the next group starts
            groupPrev = tmp

        return dummy.next


    def get_k(self, curr, k):
        # Iterate until you get to k
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr