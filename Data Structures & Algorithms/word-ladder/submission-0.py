class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Adjacency list with pattern matching technique
        # Time and Space: O(m ^ 2 * n), where m is the length of the word and n is the number of wordList

        # Return 0 if the final word is not in the wordList
        if endWord not in wordList:
            return 0

        # Part 1: Create adjacency list based on patterns differing by 1
        # Create dictionary for adj list
        neighbors = {}
        # Add the beginWord to wordList to iterate over iterate
        wordList.append(beginWord)

        # Iterate over words and add patterns
        for word in wordList:
            # Iterate over letters
            for i in range(len(word)):
                # Create pattern
                pattern = word[:i] + "*" + word[i + 1:]
                # Check if pattern exists in neighbors
                if pattern not in neighbors:
                    neighbors[pattern] = []

                # Append the word to the pattern's list
                neighbors[pattern].append(word)

        
        # Part 2: standard BFS using set and queue
        # Initialize set and queue using the beginWord
        visit = set([beginWord])
        queue = deque([beginWord])

        # Set result to 1 initially because length of result chain is 1 with beginWord
        res = 1

        # Iterate while the queue exists
        while queue:
            # Iterate through each level
            for _ in range(len(queue)):
                # Pop the word from the level
                word = queue.popleft()

                # Check if the word is the endWord and return the result
                if word == endWord:
                    return res

                # Pattern match
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    # Iterate over the items in that pattern and add to the queue
                    for nei in neighbors[pattern]:
                        # If the neighbor has not been visited, add it to the set and queue
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)

            res += 1

        # Return 0 in the case that the endWord cannot be reached
        return 0