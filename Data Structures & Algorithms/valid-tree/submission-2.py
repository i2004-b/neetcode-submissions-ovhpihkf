class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS Solution
        # Check if n is 0

        if not n:
            return True

        # Create adjacency list
        adj_list = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # Declare a set to hold visited values
        visit = set()

        # Declare dfs function
        def dfs(node, prev):
            # Check if the node has been visited
            if node in visit:
                return False

            # Add node to visit
            visit.add(node)

            # Iterate through the children of the node to run dfs
            for c in adj_list[node]:
                # Check if the child is the parent (and skip if it is)
                if c == prev:
                    continue
                # Run dfs
                if not dfs(c, node):
                    return False
                
            return True

        # Run dfs and check its output as well as length comparison
        return dfs(0, -1) and len(visit) == n
                
