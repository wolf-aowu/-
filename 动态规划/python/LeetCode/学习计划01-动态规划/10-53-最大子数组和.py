class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        dp 的含义是包含 nums[i] 的最大子数组的和
        状态转移公式：max(dp[i - 1] + nums[i], nums[i]))
        该公式的意思是带 i - 1 的子数组和加上 i 还没有 i 大，
        那么自然前面的子数组就要舍去，从 i 开始才会有肯能是最大的子数组，
        但是还存在一种情况是子数组和在 x 到达了峰值，后面的 i 能使子数组和下降，
        但是下降后的值仍然大于 i，例如：[4,-1,2,1,-5]，[4,-1,2,1] 到达峰值，
        dp 是 6，而 [4,-1,2,1,-5] 的 dp 是 1，但是 1 > -5
        所以，该公式得到的 dp 最后一位不是最大子数组和，但是最大子数组和一定在 dp 中
        '''
        length = len(nums)
        dp = [nums[0]]
        for i in range(1, length):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
        return max(dp)
