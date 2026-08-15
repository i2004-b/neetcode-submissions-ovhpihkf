class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Need adjacency list mapping courses and their pre-requisites
        pre_map = {i: [] for i in range(numCourses)}

        # Add the prereqs to the preMap
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # Have a set holding visited items
        visit = set()

        # Define dfs function
        def dfs(crs):
            # Base Cases
            # 1) if crs has been visited, return False
            if crs in visit:
                return False
            # 2) if crs's list is empty, return True
            if pre_map[crs] == []:
                return True

            # Add course to visit
            visit.add(crs)

            # Loop through the prereqs
            for pre in pre_map[crs]:
                # If returns false, return false
                if not dfs(pre):
                    return False

            # Remove current node from visit
            visit.remove(crs)

            # Set list to []
            pre_map[crs] = []

            # Return true
            return True

        # Run through the courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True