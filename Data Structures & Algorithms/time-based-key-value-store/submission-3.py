class TimeMap:

    def __init__(self):
        # Declare a hashmap that will hold the values
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        # Check if the key does not exist in the hashmap
        if key not in self.store:
            # Initialize the value to be an empty list
            self.store[key] = []

        # Append the [value, timestamp] to the key's list
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # Initialize the result to be empty --> this will be returned in the case that the key DNE or that there is not a valid value
        res = ""
        # Get the values list of lists for the key
        values = self.store.get(key, [])

        # Initialize pointers
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            # Check if the value at mid is an exact match
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                # Set result to this value as it would still be valid
                res = values[mid][0]
                # Update the left pointer
                l = mid + 1
            else:
                # Just update the right pointer
                r = mid - 1

        # Return res
        return res
        
