class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                total = ast + stack[-1]

                if total < 0:
                    stack.pop()
                elif total > 0:
                    ast = 0
                else:
                    ast = 0
                    stack.pop()

            if ast:
                stack.append(ast)

        return stack