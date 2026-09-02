class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # DFS Solution
        # Time: O(V * E)
        # Space: O(V + E)

        # Strategy:
        # Use adjacency list to create connections
        # Use a dictionary to hold the minimum distances from the source to the networkDelayTime
        # Create a dfs function that takes in a node and the time it takes for the network to propagate a message to it
        # Exit the recursive call if the time inputted to the function is greater than the time on log
        # Set the time to get to the node to the new time
        # Run dfs for the neighbors of the node

        adj = {}

        for i in range(1, n + 1):
            adj[i] = []

        # u --> source, v --> target, t --> time
        for u, v, t in times:
            adj[u].append((v, t))

        # Declare dictionary of distances
        dist = {node : float("inf") for node in range(1, n + 1)}

        # DFS function
        def dfs(node, time):
            # Base Case
            if time >= dist[node]:
                return

            dist[node] = time

            # Run dfs on neighbors
            for nei, t in adj[node]:
                # Add the current time as well
                dfs(nei, t + time)

        # Call dfs
        dfs(k, 0)
        # Set the result to be the max value
        res = max(dist.values())
        # Return the result if it is less than infinity, else return -1
        return res if res < float("inf") else -1
