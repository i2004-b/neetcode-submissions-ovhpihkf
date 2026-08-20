class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Find the number of nodes (n)
        # n = to the number of edges because of the redundant edge
        nodes = len(edges)

        # Create initialize dictionaries for parent nodes and the rank of a node
        parent = {}
        rank = {}

        # Iterate through nodes, setting node to be parent itself 
        # Set ranks to be 0
        for n in range(1, nodes + 1): # Has to run from 1 to N + 1 because nodes labeled from 1 - n
            parent[n] = n
            rank[n] = 0

        
        # Create a helper function to find the parent
        def find(node):
            # Find parent
            p = parent[node]

            # Iterate while the parent is not the same as the node (means you got to the top)
            while p != parent[p]:
                # Reassign the parent
                parent[p] = parent[parent[p]]
                # Reassign p's parent
                p = parent[p]

            return p

        
        # Create helper function to unionize
        def union(n1, n2):
            # Get parents of both
            p1, p2 = find(n1), find(n2)

            # If parents of both are the same, return False (there is a cycle)
            if p1 == p2:
                return False

            # When parents are not the same, join by rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2] += 1

            return True

        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2] 