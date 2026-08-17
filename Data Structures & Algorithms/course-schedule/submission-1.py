class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create map for the course numbers to lists that will hold the pre-reqs
        pre_map = {i: [] for i in range(numCourses)}

        # Add the pre_reqs to the lists
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # Have a visit set for courses that have been visited
        visit = set()

        # Write dfs algorithm that goes through the courses
        def dfs(crs):
            # If the course is in the visit set, return False
            if crs in visit:
                return False
            # If the course's list is empty, return True (everything satsified)
            if pre_map[crs] == []:
                return True

            # Add the course to the visit set
            visit.add(crs)

            # Run dfs for each pre-req
            for pre in pre_map[crs]:
                # If false, return False
                if not dfs(pre):
                    return False

            # Remove the course from visit
            visit.remove(crs)
            # Set the course's list to empty
            pre_map[crs] = []

            # Return true
            return True

        # Call dfs on the courses
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True