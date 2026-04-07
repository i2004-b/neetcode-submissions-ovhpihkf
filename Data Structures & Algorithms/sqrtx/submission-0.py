class Solution:
    def mySqrt(self, x: int) -> int:
        saved = 0
        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid

            if squared > x:
                right = mid - 1
            elif squared < x:
                if squared > saved:
                    saved = mid
                left = mid + 1
            else:
                return mid

        return saved