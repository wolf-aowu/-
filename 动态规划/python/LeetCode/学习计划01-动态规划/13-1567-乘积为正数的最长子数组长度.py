from operator import ne
from turtle import pos


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        positive = [1 if nums[0] > 0 else 0] + [0] * (length - 1)
        negative = [1 if nums[0] < 0 else 0] + [0] * (length - 1)
        for i in range(1,length):
            if nums[i] > 0:
                positive[i] = positive[i - 1] + 1
                negative[i] = negative[i - 1] + 1
            elif nums[i] == 0:
                positive[i] = positive[i - 1] + 1
                negative[i] = 0
            else:
                positive[i] = max(positive[i - 1],negative[i - 1] + 1)
                negative[i] = max(positive[i - 1] + 1,negative[i - 1])
        return positive[-1]
