class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Check if the grid exists
        if not grid:
            return 0

        # Get rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # Declare queue (initially holds the rotten fruit)
        queue = deque()
        # Declare visit set
        visit = set()

        # Declare count varibale to track the number of 1s
        self.count_1 = 0

        # Iterate through grid to update count of 1s and add rotten fruit to queue
        for r in range(ROWS):
            for c in range(COLS):
                # If it is fresh fruit, add to count
                if grid[r][c] == 1:
                    self.count_1 += 1
                # If it is rotten, add to queue and visit
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    visit.add((r, c))

        # Declare variable to track minutes
        minutes = 0

        # Helper function to add values
        def add(r, c):
            # Base case: check bounds, if the cell is empty, or if the val has been visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visit):
                return

            # Add coordinate to the queue
            queue.append((r, c))
            # Add coordinate to visit
            visit.add((r, c))
            # Update count of 1s
            self.count_1 -= 1

        # Iterate while the queue exists:
        while self.count_1 > 0 and queue:
            # Iterate through each level
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Add the neighbors
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)

            # Update minutes
            minutes = minutes + 1 if queue else minutes + 0

        # Return minutes if all fresh fruit has become rotten, else return -1
        return minutes if self.count_1 == 0 else -1



