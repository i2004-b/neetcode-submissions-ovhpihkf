class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Get number of edges
        N = len(edges) # Same as the number of vertices because of the cycle

        # Declare and initialize parent and rank dictionaries
        parent = {}
        rank = {}

        for i in range(1, N + 1):
            parent[i] = i
            rank[i] = 0

        # Helper find function (finds parent --> path compression done as well)
        def find(node):
            # Get current parent
            p = parent[node]

            # Iterate while parent is not self
            while p != parent[p]:
                # Assign parent to parent of the parent (grandparent)
                parent[p] = parent[parent[p]]
                # Reassign current p
                p = parent[p]

            # Return p
            return p

        # Helper union function
        def union(n1, n2):
            # Get parents of both nodes
            p1, p2 = find(n1), find(n2)

            # Check that the parents are not equal
            if p1 == p2:
                return False

            # Unionize based on rank
            if rank[p1] > rank[p2]:
                # Assign parent of p2 as p1
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                # Arbitrary
                parent[p1] = p2
                rank[p2] += 1

            return True

        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]
