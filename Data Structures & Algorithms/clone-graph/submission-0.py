"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS Method
        # T: O(V + E)
        # S: O(V)

        # Check if the given node exists
        if not node:
            return None

        # Declare hashmap --> will map og to duplicate node
        # Helps us avoid duplicating nodes
        old_to_new = {}

        # Create dfs helper function
        def dfs(node):
            # If the node is already in the hashmap, return it (don't need to make a new copy)
            if node in old_to_new:
                return old_to_new[node]

            # Add the new node to the map along with its duplicate
            old_to_new[node] = Node(node.val)

            # Iterate through the neighbors of the original node
            for neighbor in node.neighbors:
                # run dfs and add to the neighbors
                old_to_new[node].neighbors.append(dfs(neighbor))

            return old_to_new[node]

        return dfs(node)

            