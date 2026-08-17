class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Check if n is 0. This means it is an empty graph, and thus a valid tree
        if not n:
            return True

        # Create adjacency list
        adj_list = {i : [] for i in range(n)}
        # Add values
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # Create a queue --> holds tuples: (node, parent)
        queue = deque([(0, -1)])
        # Create visit set
        visit = set()
        visit.add(0)

        # Iterate while the queue exists
        while queue:
            # Popleft
            node, parent = queue.popleft()

            # Iterate through children of the node
            for c in adj_list[node]:
                # If the child is the parent, continue to next iteration
                if c == parent:
                    continue
                # Check if the child has been visited
                if c in visit:
                    return False

                # Add the (child, parent) to the queue
                queue.append((c, node))
                # Add to visit
                visit.add(c)

        # Check that the set length equals n
        return len(visit) == n