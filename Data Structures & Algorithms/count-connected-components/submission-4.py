class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS Approach to counting components
        # DFS goes through a whole components
        # T: O(V + E), S: O(V + E) (Recursive stack)

        # Create adj_list
        adj_list = {i : [] for i in range(n)}

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # Keep track of visited nodes
        visit = set()

        # Declare helper dfs function
        def dfs(node):
            # Base case: if the node has been visited, return
            if node in visit:
                return

            # Add the node to the visit set
            visit.add(node)

            # Iterate through the connections the node has
            for conn in adj_list[node]:
                # Run dfs if not in visit
                if conn not in visit:
                    dfs(conn)

            return

        # Declare var to store components
        components = 0

        # Iterate through nodes
        for i in range(n):
            # Run dfs if i is not in visit
            if i not in visit:
                dfs(i)
                components += 1

        return components

            