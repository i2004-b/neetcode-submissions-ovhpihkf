class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        adj_list = {i : [] for i in range(n)}

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # Create array tracking which nodes have been visited
        visit = [False] * n

        # Declare bfs helper function
        def bfs(node):
            # Initialize queue with node
            queue = deque([node])

            # Update visit status of node
            visit[node] = True

            # Iterate while the queue exists
            while queue:
                # Pop from queue
                curr = queue.popleft()

                # Iterate through neighbors
                for nei in adj_list[curr]:
                    # Check that the neighbor has not been visited
                    if not visit[nei]:
                        # Add to the queue
                        queue.append(nei)
                        # Update status
                        visit[nei] = True

        # Variable to track components
        components = 0
        # Iterate through nodes
        for node in range(n):
            # If the node hasn't been visited, run bfs and upfate counter
            if not visit[node]:
                bfs(node)
                components += 1

        return components