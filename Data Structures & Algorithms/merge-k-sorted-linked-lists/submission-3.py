# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ Recursive Solution Re-attempt"""
        # Check if the lists array exists and that it has at least 1 element
        if not lists or len(lists) == 0:
            return None

        return self.divide(lists, 0, len(lists) - 1)


    # This function divides into the separate lists
    def divide(self, lists, l, r):
        # Base case 1: check that l is not greater than r
        if l > r:
            return None
        # Base case 2: check if l == r, and return the list at that point
        if l == r:
            return lists[l]

        # Calculate the middle index
        mid = (r + l) // 2

        # Call the divide functions again for the left and the right "subtrees"
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        # Now, merge the two lists
        return self.merge(left, right)


    # This function is a standard method of merging two linked lists
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