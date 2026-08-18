class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Create adj list
        adj_list = { i : [] for i in range(n)}

        # Add values (undirected so add both ways)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        components = 0
        
        # Nodes that have been visited
        visit = set()

        # Create helper function for dfs
        def dfs(node, parent):
            # if node in visit:
            #     return

            visit.add(node)

            # Go through children
            for conn in adj_list[node]:
                if conn == parent or conn in visit:
                    continue
                
                dfs(conn, node)

            return


        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                components += 1

        return components



        

