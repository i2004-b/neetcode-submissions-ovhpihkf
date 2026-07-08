"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Most efficient solution: no extra space needed (besides the output list)
        # T: O(n), S: O(n)

        # Check that the head exists
        if not head:
            return None

        # Set a pointer to the head
        l1 = head
        # Iterate while l1 is not None
        # Merged both the original list and copied list so that the copied elements come before respective originals
        while l1:
            # Create a new node with val of l1
            l2 = Node(l1.val)
            # Connect l2.next to what l1.next is pointing to
            l2.next = l1.next
            # Set l1.next to be pointing to l2
            l1.next = l2
            # Increment l1
            l1 = l1.next.next

        # Set a new head for the copied list
        newHead = head.next

        # Set a pointer again to the head
        l1 = head
        # This loop matches nodes with the random pointers
        # Iterate while l1 exists
        while l1:
            # Check that l1 has a valid random pointer
            # If l1 is None, nothing extra to do as the node is initialized with Null
            if l1.random:
                # Connect the random pointer of l2 (l1.next) to the node after l1.random (which is the copy)
                l1.next.random = l1.random.next
            # Increment l1 (skip over copied element)
            l1 = l1.next.next

        # Set pointer again to be the head
        l1 = head
        # This loop separates out both lists
        # Iterate while l1 exists
        while l1:
            # Have pointer to l2
            l2 = l1.next
            # Connext l1.next to original next link
            l1.next = l1.next.next
            # Connect l2 as long as the next value is valid
            if l2.next: # Otherwise, at the end of the list
                l2.next = l2.next.next
            
            # Increment l1
            l1 = l1.next

        # Return the newHead
        return newHead


        