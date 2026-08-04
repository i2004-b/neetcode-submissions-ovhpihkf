class Twitter:

    def __init__(self):
        # Initialize count for tracking the time
        self.count = 0
        # Initialize the tweepMap
        self.tweetMap = defaultdict(list)
        # Initialize the followMap, which will use sets as values for each adding and removing
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add new tweet to the end of the list, along with the current count
        self.tweetMap[userId].append([self.count, tweetId])
        # Update the count
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Array to save the results
        res = []
        # Declare heap
        heap = []
        # Add the user to its own follower list
        self.followMap[userId].add(userId)

        if len(self.followMap[userId]) >= 10:
            max_heap = []
            for follower in self.followMap[userId]:
                if follower in self.tweetMap:
                    index = len(self.tweetMap[follower]) - 1
                    count, tweetID = self.tweetMap[follower][index]
                    heapq.heappush(max_heap, [count, tweetID, follower, index - 1])

                    if len(max_heap) > 10:
                        heapq.heappop(max_heap)

            # Iterate over the max_heap and add to the heap
            while max_heap:
                heapq.heappush(heap, heapq.heappop(max_heap))
        else:
            # Iterate through the followers
            for follower in self.followMap[userId]:
                # Check that the follower has tweets
                if follower in self.tweetMap:
                    # Get the index of the last element
                    index = len(self.tweetMap[follower]) - 1
                    # Get the count and tweet ID
                    count, tweetID = self.tweetMap[follower][index]
                    # Add to the heap
                    heapq.heappush(heap, [count, tweetID, follower, index - 1])

        while heap and len(res) < 10:
            # Pop and add that value to head
            count, tweetID, follower, index = heapq.heappop(heap)
            res.append(tweetID)

            if index >= 0:
                count, tweetID = self.tweetMap[follower][index]
                heapq.heappush(heap, [count, tweetID, follower, index - 1])

        return res





























    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the followMap
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followeeId is the follower is following them
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
