from typing import List


class Solution:
    def func_1(self, nums: List[int]) -> int:
        '''
        dp[i] 就是从 0 开始到 i - 2 中 dp 最大现金加当前房间现金
        也就是到下标为前 i-2 的房间能偷到的最大现金加当前房间现金
        '''
        roomCount = len(nums)
        if roomCount == 0:
            return 0
        elif roomCount == 1:
            return nums[0]
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, roomCount):
            dp.append(max(dp[:-1]) + nums[i])
        return max(dp)

    def func_2(self, nums: List[int]) -> int:
        '''
        func_1 的优化版，解题思路：
        dp 是到当前房间时的最大现金，那么只有两种情况：
        1. dp[i - 2] + nums[i]
        2. dp[i - 1]
        按照 dp 的意思，dp[i - 1] 存在下标 i - 1 没有偷的情况，
        也就是此时 dp[i - 1] = dp[i - 2]，那么这种情况的结果其实就是情况 1 的结果
        所以，只要获取上面两种情况的最大值即可
        '''
        roomCount = len(nums)
        if roomCount == 0:
            return 0
        elif roomCount == 1:
            return nums[0]
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, roomCount):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        return dp[-1]

    def func_3(self, nums: List[int]) -> int:
        '''
        func_2 的优化版，降低空间复杂度，使用滚动数组的方法
        因为 dp[i] 的状态实际只依赖于 dp[i - 1] 和 dp[i - 2]
        所以，可以只使用两个变量保存 dp[i - 1] 和 dp[i - 2]
        '''
        roomCount = len(nums)
        if roomCount == 0:
            return 0
        elif roomCount == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, roomCount):
            res = max(first + nums[i], second)
            first, second = second, res
        return second

    def rob(self, nums: List[int]) -> int:
        return self.func_2(nums)
