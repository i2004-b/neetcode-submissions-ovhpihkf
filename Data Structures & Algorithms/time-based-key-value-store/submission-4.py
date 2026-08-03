class TimeMap:

    def __init__(self):
        # Need to initialize a dictionary to map a key with list of pairs
        # The pairs are a list of length two --> [value, timestamp]

        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Set adds the value to the dictionary
        # Add an empty list to the key if it is new
        if key not in self.store:
            self.store[key] = []

        # Add the pair to the list
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Get the result
        # Either get the value for the key at the timestamp OR get the value closest to it that is before it

        # Initialize a res variable that is empty
        # This will return empty if the list DNE or such a value DNE
        res = ""

        # Get the list for the key
        # If it DNE, will return an empty list
        values = self.store.get(key, [])

        # Declare pointers for binary search
        l, r = 0, len(values) - 1

        # Run binary search
        while l <= r:
            # Calculate the middle
            mid = (l + r) // 2

            # Check if the value is equal to timestamp
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                # If it is less, update the result and move left pointer
                res = values[mid][0]
                l = mid + 1
            else:
                # Just update right pointer
                r = mid - 1

        # Returns empty string or the closest value to the actual timestamp
        return res

        
