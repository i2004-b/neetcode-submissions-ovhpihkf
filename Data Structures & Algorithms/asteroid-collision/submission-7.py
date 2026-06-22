class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Solution Description:
        T: O(n), S: O(n)

        A stack can be used to solve this problem.
        Keep track of the asteroids that are coming using a stack and check whether or not collisions occur.
        Collisions can only occur if the top of the stack is positive and the current asteroid is negative.
        Iterate through the stack while the stack exists, the top of the stack is positive, and the current asteroid is negative.
            Find the sum of the top of the stack and the asteroid.
            If the sum < 0: the asteroid has greater magnitude so pop from the stack
            If the sum > 0: set the asteroid to be 0 (as we are guaranteed no asteroid is 0)
            If the sum == 0: pop from the stack and set the asteroid to 0 to ensure the while loop does not execute

        Append the asteroid to the stack as long as it is not 0
        """

        # Declare stack
        stack = []

        # Iterate through the asteroids
        for a in asteroids:
            # Iterate through the stack and check that a collision can occur
            while stack and stack[-1] > 0 and a < 0:
                # Find the sum of the top of the stack and the asteroid
                diff = stack[-1] + a

                if diff < 0:
                    # Asteroid has larger magnitude
                    stack.pop()
                elif diff > 0:
                    # Top of the stack has larger magnitude so "destroy" asteroid
                    a = 0
                else:
                    # Both are equal in magnitude so destroy both
                    stack.pop()
                    a = 0

            # Add the value to the stack as long as it has not been set to 0
            if a:
                stack.append(a)
        
        return stack
