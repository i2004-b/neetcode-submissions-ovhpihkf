class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Method using 2 sets --> one to see if the course has been visited (everything fulfilled), another to detect cycles
        
        # Declare adjacency list
        pre_map = {i : [] for i in range(numCourses)}

        # Add the prerequisites to list of the specific course
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # Declare two sets --> one for visit and another for cycle detection
        visit, cycle = set(), set()

        # Declare output list
        output = []

        # Have a dfs helper function
        def dfs(crs):
            # Two base cases
            # Base Case 1: if the crs is in the current cycle, return False
            if crs in cycle:
                return False
            # Base Case 2: if the crs has been visited (fulfilled), return True
            if crs in visit:
                return True

            # Add the crs to the cycle set
            cycle.add(crs)

            # Run dfs on the prereqs of the crs
            for pre in pre_map[crs]:
                # Return false if dfs comes back false
                if not dfs(pre):
                    return False

            # Remove the crs from cycle
            cycle.remove(crs)

            # Add the crs to the visit set (successfully matched pre-reqs)
            visit.add(crs)
            # Add the course to the output as well
            output.append(crs)

            # Return True
            return True

        # Run dfs on the prereqs of the course
        for i in range(numCourses):
            # If dfs returns false, return an empty list
            if not dfs(i):
                return []

        # Return output list
        return output