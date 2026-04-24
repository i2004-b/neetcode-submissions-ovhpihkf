class Solution:
    def rob(self, nums: List[int]) -> int:
        money = []

        for i in range(len(nums)):
            if i == 0:
                money.append(nums[0])
            elif i == 1:
                money.append(max(nums[0], nums[1]))
            else:
                money.append(max(money[i - 1], nums[i] + money[i - 2]))

        return money[-1]