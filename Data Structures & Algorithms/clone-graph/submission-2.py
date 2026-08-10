"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        # Check if the node exists
        if not node: # Check initial node, not the nodes afterward
            return None

        # Declare hashmap to keep track of the values that you see
        old_to_new = {}

        # Declare helper dfs function
        def dfs(node): # Node (original) is the only input
            # If the node has already been added to the hashmap, return the duplicated node
            if node in old_to_new:
                return old_to_new[node]

            # Make a copy of the current node
            copy = Node(node.val)

            # Add the copy to the hashmap
            old_to_new[node] = copy

            # Iterate through the neighbors of the original node and add to neighbors of the copy
            for nei in node.neighbors:
                old_to_new[node].neighbors.append(dfs(nei))

            # Return the newly created node
            return copy

        return dfs(node)