class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a heap to keep track of the closest
        # Want to create a max heap so that the "max distance" is replaced when a closer one is found

        # Max_heap
        max_heap = []

        # Result array
        res = []

        # Iterate through the points array
        for coord in points:
            # Unpack the coordinate
            x, y = coord
            # Calculate the distance from the origin
            distance = math.sqrt(x**2 + y**2) # No need to subtract because at the origin
            # Add the negative of the value into the heap as tuple with the coordinate
            heapq.heappush(max_heap, (-distance, [x, y]))

            # Check if the distance is greater than k
            # Can use conditional because iterating point by point
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Iterate through the heap and add the points to the result
        for dist, point in max_heap:
            res.append(point)


        return res

        

        