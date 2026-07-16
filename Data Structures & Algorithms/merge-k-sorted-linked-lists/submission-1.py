# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ 
        Recursive Solution:
        This solution is similar to merge sort.
        You will need two helper functions (one to divide into single lists and another to combine lists).
        In this main function do the following:
            Check that the lists array is valid and that it has more than 0 elements
        
        Define the following helper functions:
            Divide: This function divides the lists (similar to how merge sort does)
            Merge: This function merges two LL

        Complexity:
        T: O(nlogk)
        S: O(logk)
        """

        # Base Case: check that the list exists and that there is at least one element
        if not lists or len(lists) == 0:
            return None
        # Call the divide function and return the result
        return self.divide(lists, 0, len(lists) - 1)


    def divide(self, lists, l, r):
        # Check that left has not surpassed r
        if l > r:
            return None
        # Check that l = r; if so, return the list at that location
        if l == r:
            return lists[l]

        # Calculate a middle point
        mid = (r + l) // 2
        # Call the divide function on the two haves
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        # Call the merge function
        return self.merge(left, right)


    def merge(self, l1, l2):
        # Merge two LL so declare a dummy node and a pointer to it
        pntr = dummy = ListNode()

        # Iterate while both lists are in range
        while l1 and l2:
            # If l1 val is less than or equal to it, point to that value
            if l1.val <= l2.val:
                pntr.next = l1
                l1 = l1.next
            else:
                pntr.next = l2
                l2 = l2.next
            # Increment pointer
            pntr = pntr.next

        # Check if any of the ists have any remaining elements
        if l1:
            pntr.next = l1
        if l2:
            pntr.next = l2

        # Return dummy.next
        return dummy.next
