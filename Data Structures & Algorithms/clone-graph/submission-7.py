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
        old_to_new = {}

        # Run bfs 
        def bfs(node):
            if not node:
                old_to_new[node] = None
                return
            # Create a copy of the node
            
            old_to_new[node] = Node(node.val)

            queue = deque()
            queue.append(node)

            while queue:
                curr = queue.popleft()

                # Add the neighbors
                for n in curr.neighbors:
                    # Add the neighbor to the hashmap is not already in it
                    if n not in old_to_new:
                        old_to_new[n] = Node(n.val)
                        queue.append(n)
                    # Connect current node to the neighbor 
                    old_to_new[curr].neighbors.append(old_to_new[n])
                    # Add neighbor to the queue
                    

            return node


                


        bfs(node)
        return old_to_new[node]


        """
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
        """
        