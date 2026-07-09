# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        curr = l1
        power = 0
        while curr:
            num1 = curr.val * (pow(10, power)) + num1
            power += 1
            curr = curr.next

        curr = l2
        power = 0
        while curr:
            num2 = curr.val * pow(10, power) + num2
            power += 1
            curr = curr.next

        total = num1 + num2
        string_num = str(total)

        # Pointer to the end
        r = len(string_num) - 1

        dummy = pntr = ListNode()

        while r > -1:
            pntr.next = ListNode(int(string_num[r]))
            pntr = pntr.next
            r -= 1
        
        return dummy.next