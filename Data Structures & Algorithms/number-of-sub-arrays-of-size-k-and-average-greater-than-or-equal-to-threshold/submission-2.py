class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Declare variable to hold current sum of the sub-array
        summed = 0
        # Have count for number of subarrays greater than or equal to threshold
        count = 0
        # Update left pointer
        l = 0

        # Iterate through arr
        for r in range(len(arr)):
            # Add the new value to the sum
            summed += arr[r]
            
            # If you are out of range, check averages
            if r - l == k - 1:
                # Calculate average
                avg = summed / k
                # Check if avg greater than threshold
                if avg >= threshold:
                    # Update count
                    count += 1
                # Take away from summed the current l value
                summed -= arr[l]
                # Increment l
                l += 1

            

        return count