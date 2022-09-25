from typing import List


class Solution:
    def func_1(self, nums: List[int]) -> int:
        '''
        乘法不能完全按照加法来，因为有一个是负数时，积会变小，有两个时，又会变大
        例如：[-2,4,-3]，dp[0] = -2，dp[1] = 4，dp[2] = -3，实际答案应该是 24
        可以进行分类讨论：
        当有一个是负数时，我们希望负数尽可能的大；
        当有两个负数时，我们希望负数尽可能的小，这样两个负数相乘时的结果越大。
        所以，我们可以再维护一个dp，专门用来放以 i 结尾的最小子数组的乘积，
        然后获取 dpmin[i - 1] * nums[i]、dpmax[i - 1] * nums[i] 和 nums[i] 中最大的
        '''
        length = len(nums)
        if nums == 1:
            return nums[0]
        dpmax = [nums[0]]
        dpmin = [nums[0]]
        for i in range(1, length):
            dpmin.append(min(dpmin[i - 1] * nums[i],
                         min(dpmax[i - 1] * nums[i], nums[i])))
            dpmax.append(max(dpmax[i - 1] * nums[i],
                         max(dpmin[i - 1] * nums[i], nums[i])))
        return max(dpmax)

    def func_2(self, nums: List[int]) -> int:
        '''
        对 func_1 进行空间复杂度的优化，采用滚动数组
        '''
        length = len(nums)
        dpmax = nums[0]
        dpmin = nums[0]
        res = nums[0]
        for i in range(1, length):
            old_dpmax = dpmax
            dpmax = max(dpmax * nums[i], max(dpmin * nums[i], nums[i]))
            dpmin = min(dpmin * nums[i], min(old_dpmax * nums[i], nums[i]))
            res = max(res, dpmax)
        return res

    def maxProduct(self, nums: List[int]) -> int:
        return self.func_2(nums)
