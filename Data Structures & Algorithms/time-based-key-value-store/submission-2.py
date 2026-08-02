class TimeMap:

    def __init__(self):
        # Set hashmap with values defaulted to be a list 
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if not self.time_map[key] or timestamp < self.time_map[key][0][0]:
            return ""
        # Binary search
        l, r = 0, len(self.time_map[key]) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.time_map[key][mid][0] < timestamp:
                l = mid + 1
            elif self.time_map[key][mid][0] > timestamp:
                r = mid - 1
            else:
                return self.time_map[key][mid][1]

        return self.time_map[key][r][1]

        
        
