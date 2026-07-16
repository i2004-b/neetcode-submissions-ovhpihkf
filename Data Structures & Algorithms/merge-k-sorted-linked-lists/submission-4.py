# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ Iterative divide and conquer re-attempt"""
        # Base case: check that the lists exist and that there is at least one in there
        if not lists or len(lists) == 0:
            return None

        # Iterate while lists has more than 1 element
        while len(lists) > 1:
            # Declare an array to hold the merged lists
            merged = []

            # Iterate through the lists and increment by 2
            for i in range(0, len(lists), 2):
                # list 1 is at location i
                l1 = lists[i]
                # list 2 is at location i + 1, but check that it is in bounds
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge these two lists and add them to the merged array
                merged.append(self.merge(l1, l2))
            # Set lists equal to merged
            lists = merged

        return lists[0]


    def merge(self, l1, l2):
        # Declare a dummy node and a pntr to it
        pntr = dummy = ListNode()

        # Iterate while both lists exist
        while l1 and l2:
            # Check values
            if l1.val <= l2.val:
                pntr.next = l1
                l1 = l1.next
            else:
                pntr.next = l2
                l2 = l2.next
            # Update pntr
            pntr = pntr.next

        # Add remaining nodes
        if l1:
            pntr.next = l1
        if l2:
            pntr.next = l2

        # Return dummy.next
        return dummy.next