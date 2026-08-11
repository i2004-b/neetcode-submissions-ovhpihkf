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
        # Create deep copy

        # Check if the node exists
        if not node:
            return None

        # Create a hashmap to keep track of the nodes created
        old_to_new = {}

        # Declare helper recursive dfs function to iterate through and create the copy
        def dfs(node):
            # Check if the node has already been created. If so, return
            if node in old_to_new:
                # Return copy which is the value of the key
                return old_to_new[node]

            # What to do if a new node

            # Create copy
            copy = Node(node.val)
            # Put the copy into the hashmap with the original
            old_to_new[node] = copy

            # Iterate through the neighbors of the original
            for nei in node.neighbors:
                # Add the neighbors to the current node's list
                copy.neighbors.append(dfs(nei))

            # Return the copied node
            return copy


        return dfs(node)