"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS Iterative solution
        # T: O(V + E)
        # S: O(V)

        # Check if the node exists
        if not node:
            return None

        # Create hashmap for old to new Nodes
        old_to_new = {}

        # Add initial node to hashmap
        old_to_new[node] = Node(node.val)

        # Create queue that is initialized with the original node
        queue = deque([node])

        # Iterate while the queue exists
        while queue:
            # Pop from the queue
            curr = queue.popleft()

            # Iterate for the neighbors of the current node
            for neighbor in curr.neighbors:
                # If the neighbor has not been added to the hashmap, add it and add it to the queue (it has not been visited)
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Add to the list the value
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        # Return where the original node was
        return old_to_new[node]