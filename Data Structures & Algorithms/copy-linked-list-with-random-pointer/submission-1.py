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
        old_to_new = {}

        def rec(node):
            if not node:
                return None
            if node in old_to_new:
                return old_to_new[node]

            new_node = Node(node.val)
            old_to_new[node] = new_node

            new_node.next = rec(node.next)

            # Set random
            new_node.random = old_to_new.get(node.random)

            return new_node

        return rec(head)