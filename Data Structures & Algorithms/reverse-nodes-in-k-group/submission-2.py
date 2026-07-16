# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if the head is non-existent
        if not head:
            return None

        # Set a dummy pointer pointing to the head
        dummy = ListNode(0, head)
        # Set another pointer that will initially point to the dummy node but will actually point to the previous group of k items
        groupPrev = dummy

        # Iterate while true
        while True:
            # Find ths kth element using a helper function
            # Pass in the end of the previous group
            kth = self.get_k(groupPrev, k)
            # Check that k is valid; break from the loop if not valid
            if not kth:
                break

            # Save the beginning of the next section; used for the loop when reversing
            groupNext = kth.next

            # Declare previous and current pointers
            # Previous intially points to the beginning of the next section
            # Curr points to wherever the previous points to
            prev, curr = kth.next, groupPrev.next

            # Iterate while curr is not in the next group
            while curr != groupNext: # Use this pointer because k's position will end up being changed
                # Save what curr is pointing to
                tmp = curr.next
                # Make curr point to prev
                curr.next = prev
                # Move previous over to curr
                prev = curr
                # Move curr over to tmp
                curr = tmp

            # Make sure that the new section is connected properly
            # First, save the location of the now last element
            last_element_location = groupPrev.next
            # Set groupPrev.next to point to the kth element as it is now the beginning of the new section
            groupPrev.next = kth
            # Set groupPrev to be where the last element is
            groupPrev = last_element_location

        return dummy.next




    def get_k(self, curr, k):
        # Iterate while curr exists and k is above 0
        while curr and k > 0:
            curr = curr.next
            k -= 1

        # return where curr ends up
        return curr