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
        # Have an array for the result
        res = []
        # Declare a heap for the most recent
        heap = []

        # Add the user to its own follower's list
        self.followMap[userId].add(userId)

        # First: add to the heap the most recent tweet for all of the people that the user follows
        for follower in self.followMap[userId]:
            # Check that the follower has a post
            if follower in self.tweetMap:
                # Get the last index
                index = len(self.tweetMap[follower]) - 1
                # Get the count and the tweetId
                count, tweetId = self.tweetMap[follower][index]
                # Add the following values to the heap: count, tweetId, follower, index - 
                # Add index - 1 because that is the next index
                # Appending here because the heap is still a list
                heap.append([count, tweetId, follower, index - 1])

        # Heapify
        heapq.heapify(heap)

        # Second: iterate while the heap exists and the length of results is <= 10
        # Pop from the heap, add it to the result, check the next value for that user and add it to the heap
        while heap and len(res) < 10:
            count, tweetId, follower, index = heapq.heappop(heap)
            # Add the tweetId to the result
            res.append(tweetId)
            # Check that the index is greater than or equal 0; if it is, add the value to the heap
            if index >= 0:
                count, tweetId = self.tweetMap[follower][index]
                # Add to the heap
                heapq.heappush(heap, [count, tweetId, follower, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the followMap
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followeeId is the follower is following them
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
