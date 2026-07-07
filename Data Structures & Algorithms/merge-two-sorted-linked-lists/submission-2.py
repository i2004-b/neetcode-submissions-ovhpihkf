# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Declare dummy node
        dummy = ListNode()

        # Set pointer equal to the dummy node
        pntr = dummy

        # Iterate while both lists are valid
        while list1 and list2:
            # If the value of list1 is less than or equal to list2, connect the pointer to it
            if list1.val <= list2.val:
                # Attach pointer next value to list1
                pntr.next = list1
                # Move pointer over
                pntr = pntr.next
                # Move list1 pointer over
                list1 = list1.next
            else:
                # Same as above but with list2
                pntr.next = list2
                pntr = pntr.next
                list2= list2.next

        # If the lists remain, attach pntr next to them
        if list1:
            pntr.next = list1
        if list2:
            pntr.next = list2

        return dummy.next