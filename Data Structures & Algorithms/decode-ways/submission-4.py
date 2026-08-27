class Solution:
    def numDecodings(self, s: str) -> int:
        # Declare cache that will hold how many ways to split at a specific location
        cache = {len(s) : 1} # Set length of s to be as base case for splitting (in the case that s is empty or s only has one item)

        # Declare dfs function
        def dfs(i): # Take in index
            # Base case 1: check if the number exists in the cache (check firat to avoid out of range error)
            if i in cache:
                return cache[i]
            # Base case 2: check if number at index is 0
            if s[i] == "0":
                return 0
            
            

            # Run dfs on the next element (treating current number as a single digit)
            res = dfs(i + 1)

            # Check if you can treat this as a two digit number
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                res += dfs(i + 2)

            # Update cache
            cache[i] = res

            return res

        return dfs(0)
