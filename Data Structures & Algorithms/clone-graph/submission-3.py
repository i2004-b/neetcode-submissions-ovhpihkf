"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS

        # Check if the node exists
        if not node:
            return None

        # Declare hashmap
        old_to_new = {}

        # Initialize the hashmap with the og node and duplicate
        old_to_new[node] = Node(node.val)

        # Declare queue and initialize with the original node
        queue = deque([node])

        # Iterate while the queue is non empty
        while queue:
            # Pop original node from the queue
            curr = queue.popleft()

            # Iterate through the neighbors in the original node
            for nei in curr.neighbors:
                # If the neighbor is not in the hashmap, add it and add it to the queue (first time being seen)
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)

                # Add to the copy's list the neighbor
                old_to_new[curr].neighbors.append(old_to_new[nei])

        return old_to_new[node]

