class Graph:
    
    def __init__(self):
        # Initialize graph as a hashmap
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        # Initialize set for points if not in graph already
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()

        # Add the dst to the src
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph and dst in self.graph and dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True

        return False


    def hasPath(self, src: int, dst: int) -> bool:
        # BFS
        queue = deque()
        queue.append(src)
        visited = set()
        visited.add(src)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == dst:
                    return True

                # Add neighbors to the graph
                for neighbor in self.graph[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        return False


