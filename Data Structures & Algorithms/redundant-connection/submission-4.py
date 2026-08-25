class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # There is redundancy, meaning the number of vertices is the same as the number of edges
        n = len(edges)

        # Use union find to track connection relationships; does not depict the actual graph
        # Need to track parents and rank
        parents = {}
        rank = {}

        # Iterate through so that everyone's parent is themselves and that rank is 0
        for i in range(1, n + 1): # Labeled from 1 to not
            parents[i] = i
            rank[i] = 0

        # Find the parent
        def find(node):
            # Save the current parent
            p = parents[node]

            # Iterate while you are not at top (parent does not equal the node)
            while p != parents[p]:
                # Reset parent
                parents[p] = parents[parents[p]]
                p = parents[p]

            return p

        def union(n1, n2):
            # Find parents
            p1, p2 = find(n1), find(n2)

            # If parents are the same, redundant
            if p1 == p2:
                return False

            # Adjust ranks
            if rank[p1] > rank[p2]:
                parents[p2] = p1
            elif rank[p1] < rank[p2]:
                parents[p1] = p2
            else:
                parents[p1] = p2
                rank[p2] += 1

            return True

        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]