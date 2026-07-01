class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        """
        DFS helper function to traverse through the matrix.
        Inputs:
            grid --> the given matrix
            r --> the row you are at
            c --> the column you are at
            visit --> a set that will hold all the visited points on that path
        Description:
            The function will recalculate the rows and columns (or can put that outside of the function to be accessed.)
            Base Case:
                Check #1:
                    - check if r and c are out of bounds (by checking if either is less than 0 or if either equals the number of rows or columns.)
                    - check to ensure that the vertex was not see already in the path.
                    - check to ensure that you have not reached a blocked point
                        -- if any of these is true, return 0
                Check #2:
                    - if you have reached the destination return 1.

            After the base cases, add the current point to the set being passed in.
            Declare a variable count (intialized to 0) which will count how many paths to the end there are from that point.
            Make recursive calls going up, down, left, and right. Ensure to increase the count accordingly.

            Before returning the final count, remember to remove the current node from the set.
        """
        def dfs(grid, r, c, visit):
            # Calculate rows and columns in grid.
            ROWS, COLS = len(grid), len(grid[0])

            # Base Case 1: Check if at a valid point, the point has not been accounted for, and the point is not blocked
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1):
                return 0
            # Base Case 2: Check that you have reached the destination
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            # Add the point to the set
            visit.add((r, c))
            
            # Declare a count variable to count the number of paths from this point to the end
            count = 0

            # Go in four directions
            count += dfs(grid, r - 1, c, visit) # up
            count += dfs(grid, r + 1, c, visit) # down
            count += dfs(grid, r, c + 1, visit) # right
            count += dfs(grid, r, c - 1, visit) # left

            # Remove the current point from the set before returning the count
            visit.remove((r, c))

            # Return the count
            return count
        
        # Call dfs on the given grid and return count
        return (dfs(grid, 0, 0, set()))


