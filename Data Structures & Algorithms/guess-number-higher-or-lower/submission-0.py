# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Assign "pointers" to the ends of the range
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2

            # Returning -1 means guess was too high
            if guess(mid) < 0:
                right = mid - 1
            elif guess(mid) > 0:
                left = mid + 1
            else:
                return mid