class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Because there is a cycle, number of edges = number of points
        N = len(edges)

        # Keep track of parents and rank
        parent = {}
        rank = {}

        # Initialize parent and rank
        for i in range(1, N + 1):
            # Set parents to themselves
            parent[i] = i
            # Set ranks to 0
            rank[i] = 0

        # Declare helper find function to find the parent
        def find(node):
            # Get parent of the node
            p = parent[node]

            # Iterate while the parent does not equal itself
            while p != parent[p]:
                # Perform path compression
                parent[p] = parent[parent[p]]
                # Set p to new parent
                p = parent[p]

            # Return the parent
            return p

        # Union the sets
        def union(n1, n2):
            # Find parents of both
            p1, p2 = find(n1), find(n2)

            # If parents are the same, return false
            if p1 == p2:
                return False

            # Union by rank, update the parent of the lesser one
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                # Arbitrary
                parent[p1] = p2
                rank[p2] += 1

            return True

        # Call union on the edges
        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]


        
