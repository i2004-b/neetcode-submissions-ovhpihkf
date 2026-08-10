class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        BFS Solution: simultaneously start from the treasures and work from there.
        Check if the grid exists
        Get number of rows and columns
        Add all the treasures to a queue first (double for loop going through grid)
        Have a dist variable that is initially 0 (treasure)
        Iterate while the queue exists
            You want to iterate level by level (for loop within while loop needed)
                Pop from the queue, and add children (all four directions) --> can use another loop or extract into a fn
            After you're done the level, increase the distance 
        """

        # Check if the grid exists
        if not grid:
            return

        # Get rows and columns
        ROWS, COLS = len(grid), len(grid[0])

        # Declare a queue that will hold each level at a time
        queue = deque()

        # Have a visit set
        visit = set()

        # Add the treasures to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # Add treasure to the queue and the set
                    queue.append((r, c))
                    visit.add((r, c))

        # Set distance variable to 0 (from the treasure)
        distance = 0

        def add_children(r, c):
            """
            Check bounds (upper and lower), check if it is water, check that it has not already been visited
            """
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visit):
                return

            queue.append((r, c))
            visit.add((r, c))
            
        # Iterate while the queue is non-empty
        while queue:
            # Iterate through each level
            for _ in range(len(queue)):
                # Pop from the queue
                r, c = queue.popleft()
                # Update distance
                grid[r][c] = distance

                # Add valid children
                add_children(r + 1, c)
                add_children(r - 1, c)
                add_children(r, c + 1)
                add_children(r, c - 1)
            
            # Update distance
            distance += 1

        