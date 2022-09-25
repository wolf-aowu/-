from typing import List


class Solution:
    def func_1(self, nums: List[int]) -> int:
        '''
        有两种情况：
        1. 如果偷窃了第一间房屋，那么最后一间房屋不能被偷窃
           所以，偷窃范围是[0,i - 1]，即 dp[i - 1]
        2. 如果偷窃了最后一间房屋，那么第一间房屋不能被偷窃
           所以，从第二间房屋开始偷，偷窃范围是[1,i-2],即dp[i - 2] + nums[i]
        注意：
        偷窃范围一定要在代码中体现出来，否则是不正确的
        '''
        roomNums = len(nums)
        if roomNums == 0:
            return 0
        elif roomNums == 1:
            return nums[0]
        elif roomNums == 2:
            return max(nums[0], nums[1])
        before = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, roomNums - 1):
            res = max(before + nums[i], second)
            before, second = second, res
        scene1 = second
        before = nums[1]
        second = max(nums[1], nums[2])
        for i in range(3, roomNums):
            res = max(before + nums[i], second)
            before, second = second, res
        scene2 = second
        return max(scene1, scene2)

    def rob_range(self, start: int, end: int, nums: List[int]) -> int:
        '''
        情况1 与 情况2 都能适用
        '''
        before = nums[start]
        second = max(nums[start], nums[start + 1])
        for i in range(start + 2, end):
            res = max(before + nums[i], second)
            before, second = second, res
        return second

    def func_2(self, nums: List[int]) -> int:
        roomNums = len(nums)
        if roomNums == 0:
            return 0
        elif roomNums == 1:
            return nums[0]
        elif roomNums == 2:
            return max(nums[0], nums[1])
        else:
            return max(self.rob_range(0, roomNums - 1, nums), self.rob_range(1, roomNums, nums))

    def rob(self, nums: List[int]) -> int:
        return self.func_2(nums)
