# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i, j = head, head.next

        while j:
            i = i.next

            if j.next:
                j = j.next.next
            else:
                j = j.next

        return i