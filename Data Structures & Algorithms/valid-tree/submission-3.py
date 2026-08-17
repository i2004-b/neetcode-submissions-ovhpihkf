class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS solution

        # Check if n is 0
        if not n:
           return True

        # Create adjacency list
        adj_list = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # Declare queue initialized with 0 and a prev of -1 (edge case)
        queue = deque([(0, -1)])
        # Create visit set and initialize with 0
        visit = set()
        visit.add(0)

        # Iterate while the queue exists
        while queue:
            # Pop from the queue
            node, parent = queue.popleft()

            # Iterate through the children of the node
            for c in adj_list[node]:
                # Check that c is not the parent
                if c == parent:
                    continue
                # Check that c is not in visit
                if c in visit:
                    return False
                
                # Add c and its parent to queue
                queue.append((c, node))
                # Add c to visit
                visit.add(c)

        return len(visit) == n