"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS Solution

        # Check if the node exists
        if not node:
            return None

        # Create hashmap mapping the old to new
        old_to_new = {}

        # Add new value to the hashmap
        old_to_new[node] = Node(node.val)

        # Declare queue and initialize with the original node
        queue = deque([node]) # Use original to access the children

        # Iterate while the queue exists
        while queue:
            # Pop from the queue
            curr = queue.popleft()

            # Add children of curr
            for nei in curr.neighbors:
                # Check if the neighbor is new
                if nei not in old_to_new:
                    # Add to hashmap
                    old_to_new[nei] = Node(nei.val)
                    # Add to queue
                    queue.append(nei)
                # Append the neighbor to the current node's copy's neighbor list
                old_to_new[curr].neighbors.append(old_to_new[nei])

        return old_to_new[node]
