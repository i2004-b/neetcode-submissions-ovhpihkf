# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Iterative divide and conquer method that uses a helper function to merge the LL together.
        In the main function do the following:
            First, check that the lists array exists and it has at least one item
            Then iterate while the lists list is longer than length 1 (if it is length 1, that means it has reached the list to return.)
                Declare a list to hold merged lists
                Iterate through the lists, but increment by 2 because you want to combine pairs.
                    Set the first list to the first index
                    Set the second list to the first index + 1, but have a check to ensure that it is in bounds as if it is an odd list, it will be out of bounds
                    Call the merge function on the first and second list and reassign lists to merged
                Once finishing the for loop, add the newly merged list to the original list

        The helper function will just merge 2 LL
        """

        # Base Case: check that the list is valid and that there is at least one element in it
        if not lists or len(lists) == 0:
            return None

        # Iterate while the lists array has more than 1 element
        while len(lists) > 1:
            # Declare an array to hold newly merged lists
            merged = []

            # Iterate over the lists array and count by two
            for i in range(0, len(lists), 2):
                # Assign the first list to the list at the current index
                l1 = lists[i]
                # Assign the second list to the list at the next index but check if in bounds
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge the lists
                merged.append(self.merge(l1, l2))
            # Append the merged lists to the lists list
            lists = merged

        # Return the remaining list
        return lists[0]

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


        