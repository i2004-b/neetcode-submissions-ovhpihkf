class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Classic dijkstra problem
        # Time: O(E * log(E))
        # Space: O(V + E)

        # Create adjacency list (dictionary)
        adj = {}

        # Initialize adj keys and values
        # 1 to n + 1 because vertices are labeled from 1 to n
        for i in range(1, n + 1):
            adj[i] = []

        # s --> source, d --> dest, w --> weight
        for s, d, w in times:
            adj[s].append((d, w))

        # Declare shortest path tracker and heap
        shortest = {}
        min_heap = [(0, k)] # Initialize with the distance to the source being 0
        t = 0

        # Iterate while heap is non empty
        while min_heap:
            # Pop from the heap
            w1, n1 = heapq.heappop(min_heap)

            # Check if the node is already in shortest
            if n1 in shortest:
                continue

            shortest[n1] = w1
            t = w1

            # Iterate and add edges and distances from n1 to the min_heap
            for n2, w2 in adj[n1]:
                # Add to min_heap as long as length has not been added
                if n2 not in shortest:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        

        return t if len(shortest) == n else -1

