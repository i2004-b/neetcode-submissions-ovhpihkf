class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        # Part 1: Initializations
        # Declare empty adjacency list 
        adj = {}

        # Add the keys to the list and initialize with lists
        for i in range(n):
            adj[i] = []

        # Add connected edges to appropriate list
        # s --> source, d --> dest, w --> weight
        for s, d, w in edges:
            adj[s].append((d, w))

        # Initialize a result dictionary
        shortest = {}

        # Initialize a min_heap with the distance to the source being 0
        min_heap = [(0, src)]

        # Part 2: Iterate while the heap exists
        while min_heap:
            # Pop min value from heap
            w1, n1 = heapq.heappop(min_heap)

            # Check if the node has already been accounted for
            if n1 in shortest:
                continue
            # Otherwise, add to shortest
            shortest[n1] = w1

            # Iterate through the connected nodes and add their values
            for n2, w2 in adj[n1]:
                # Check that the node has not already had a shortest path found
                #if n2 not in shortest:
                heapq.heappush(min_heap, (w1 + w2, n2))

            
        # Part 3: Fill with -1 any unreachable vertex
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        # Return dictionary
        return shortest
        