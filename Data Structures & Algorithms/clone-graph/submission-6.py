"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS Solution
        # Iterating through every vertex and every edge --> O(V + E) (for both T and S)

        # First, declare hashmap that will map the old to new nodes
        old_to_new = {}

        # Run dfs 
        def dfs(node):
            # Check if the node has already been added and if so, return its copy
            if node in old_to_new:
                return old_to_new[node]

            # If the node is not in the dictionary, create a copy 
            copy = Node(node.val)

            # Add copy to the dictionary
            old_to_new[node] = copy

            # Connect it to the other nodes
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        
        return dfs(node) if node else None
        