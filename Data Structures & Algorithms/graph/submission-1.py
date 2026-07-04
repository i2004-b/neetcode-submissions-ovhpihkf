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
        # To check if there is a path can either use bfs or dfs
        visit = set()

        # Create helper dfs function
        def dfs(node, target, graph):
            if node == target:
                return True

            # No need to keep track of the count/length
            # Add the node to the set
            visit.add(node)

            # Iterate and call dfs on the children
            for neighbor in graph[node]:
                if neighbor not in visit:
                    if dfs(neighbor, target, graph):
                        return True

            return False

        return dfs(src, dst, self.graph)


