class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # Declare the total number of rows and columns
        ROWS, COLS = len(grid), len(grid[0])

        # Intialize a queue and set
        queue = deque()
        visit = set()

        # Set the initial length to 0
        length = 0

        # Add the initial point to the queue and the set
        if grid[0][0] != 1:
            queue.append((0, 0))
            visit.add((0, 0))

        # Iterate while the queue exists
        while queue:
            # Check each level
            for i in range(len(queue)):
                # Pop from the left of the stack
                r, c = queue.popleft()
                # Check if you have reached the destination
                if r == ROWS - 1 and c == COLS - 1:
                    # Return the length
                    return length
                
                # Declare a list of lists that holds the directions to move in
                neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                # Iterate through the four directions
                for dr, dc in neighbors:
                    # Check the base cases: see if the directions to go in are in bounds, they are not blocked, and that it has not been visited 
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    
                    # Add to the queue and the set
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            # Increment the length
            length += 1
        
        return - 1



