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
        # Two-Pass solution
        # T: O(n), S: O(n)

        # Create a hashmap to hold the old node mapped to the new node
        # Intialize the hasmap with None pointing to None (edge case when connecting nodes together)

        old_to_new = {None: None}

        # Iterate through the list and make copies
        curr = head

        while curr:
            # Make the copy
            copy = Node(curr.val) # DO NOT copy next and random as those will point to the original list
            # Add to the dictionary
            old_to_new[curr] = copy
            # Update curr
            curr = curr.next

        # Iterate through the original list again and connect the new nodes
        # Set curr to head again
        curr = head

        while curr:
            # Get the copy
            copy = old_to_new[curr]
            # Connect the next and random pointers
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            # Update the curr variable
            curr = curr.next

        # Return the new head based on what the old head was
        return old_to_new[head]