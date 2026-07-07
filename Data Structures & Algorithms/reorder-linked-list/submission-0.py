# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Algorithm:
        1) Split list into two halves
                Find the two halves using slow and fast pointers
        2) Reverse the second half of the list
                Set last element in first half to NULL
        3) Put together the reordered LL
                Make sure to save links so you are able to jump back and forth properly
        """
        # Declare slow and fast pointers that will aid in figuring out the mid point
        slow, fast = head, head.next

        # Iterate while the fast pointer and fast.next exist (because jumping by 2)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # The second half begins at slow.next
        second = slow.next

        # Set slow.next to None to end the first half of the list and keep it separate
        slow.next = None

        # Set a previous pointer to None (needed to reverse the list)
        prev = None

        # Iterate while second is non-Null
        while second:
            # Save second.next
            tmp = second.next
            # Connext current second.next to prev
            second.next = prev
            # Update prev to be at second
            prev = second
            # Update second to be at second.next
            second = tmp

        # Set pointers for the first and second half of the array
        first, second = head, prev # Set second to previous because second goes out of bounds intially

        # Iterate while second exists
        while second:
            # Save links to next values
            tmp1, tmp2 = first.next, second.next
            # Assign first next to second
            first.next = second
            # Assign second next to tmp1
            second.next = tmp1
            # Update first and second
            first = tmp1
            second = tmp2

        
        