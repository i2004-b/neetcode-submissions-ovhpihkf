class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get rows and columns
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # Declare DFS function that visits from each side
        
        """
        Inputs:
        r --> row
        c --> column
        visit --> set
        prevHeight --> the height of the previous block
        """
        def dfs(r, c, visit, prevHeight):
            """
            Base Case:
            Return nothing if the following occurs:
                The coordinate is out of bounds
                The coordinate has already been visited
                The height is less than the previous height
            """

            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                (r, c) in visit or
                heights[r][c] < prevHeight):
                return

            # Add the node to the visit set
            visit.add((r, c))

            # Run dfs in each direction
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Iterate through the top row (Pacific) and the bottom row (Atlantic)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Iterate through the first (Pacific) and the last columns (Atlantic)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Make results array
        res = []

        # Iterate through the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If point in both sets, add to results
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
        



