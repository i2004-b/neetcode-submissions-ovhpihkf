class Solution:

    #def climbStairs(self, n: int) -> int:
        
       # one, two = 1, 1

       # for i in range(n - 1):
         #   temp = one
         #   one = one + two
         #   two = temp

        #return one

    def climbStairs(self, n: int) -> int:
        
        if n <= 3:
            return n

        point1, point2 = 2, 3

        for i in range(4, n + 1): 
            temp = point1 + point2
            point1 = point2
            point2 = temp

        return point2

