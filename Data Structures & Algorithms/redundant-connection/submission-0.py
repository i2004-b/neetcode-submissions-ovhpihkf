class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union find algorithm

        # Maintain parent (1-n)
        N = len(edges)

        # Set the parents to be the nodes themselves
        parent = [i for i in range(N + 1)]
        # Set the ranks of the nodes to be 1 initially
        rank = [1] * (N + 1)

        # Helper function to find parents
        def find(n):
            # Check if n is equal to its own parent
            if n == parent[n]:
                return parent[n]

            # Set parent to be root node
            parent[n] = find(parent[n])
            return parent[n]

        # Helper union function (takes in 2 parameters)
        def union(n1, n2):
            # Get the parents
            p1, p2 = find(n1), find(n2)

            # If the parents are the same, return False
            if p1 == p2:
                return False

            # Union by rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]