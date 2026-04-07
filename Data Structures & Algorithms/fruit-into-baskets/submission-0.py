class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Keep count of the fruits
        count = {}

        l, total, result = 0, 0, 0

        for r in range(len(fruits)):
            count[fruits[r]] = 1 + count.get(fruits[r], 0)
            total += 1

            while len(count) > 2:
                # Save the left element
                fruit = fruits[l]
                # Decrement that item from the ditionary
                count[fruit] -= 1
                # Decrement the total length 
                total -= 1
                # Increment the left pointer
                l += 1

                # Delete from the dictionary is empty
                if count[fruit] == 0:
                    count.pop(fruit)




            result = max(result, total)

        return result