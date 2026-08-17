class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Check if n is 0
        if not n:
            return True # Empty graph is a valid tree

        # Set up adjacency list
        adj_list = {i : [] for i in range(n)}

        # Add points to adjacency list
        for n1, n2 in edges:
            # Add both ways because undirected graph
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # Create visit set
        visit = set()

        # Make dfs function 
        def dfs(node, prev):
            # Check if node has been visited
            if node in visit:
                return False

            # Add the node to the visit set
            visit.add(node)

            # Run through the nodes in the adjacency list
            for i in adj_list[node]:
                # Check if i is the prev value
                if i == prev:
                    continue
                # Run dfs
                if not dfs(i, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n