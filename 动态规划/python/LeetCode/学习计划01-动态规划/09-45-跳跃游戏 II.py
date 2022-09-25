class Solution:
    def func_1(self, nums: List[int]) -> int:
        '''
        dp 含义：到达 i 时需要的最小步数
        根据题意可以得到最小不是可以到达 i 就一定能到达 i - 1，
        假设存在 dp[i - 1] > dp[i]，此时结合题意和 dp 含义可以得到 dp[i - 1] 应该为 dp[i]
        所以 dp[i - 1] <= dp[i]，即 dp 时是递增的
        所以我们应该从前往后找，找到第一个能够到达 i 的，
        此时得到的步数一定小于等于后面找到的步数，
        因此不用去管 i - 1，只需找到第一个能到达 i 的位置
        不知对错，因为超时了 T_T
        '''
        length = len(nums)
        if length == 1:
            return 0
        dp = [0] * length
        for i in range(1, length):
            for j in range(0, i):
                if j + nums[j] >= i:
                    dp[i] = dp[j] + 1
                    break
        return dp[-1]

    def func_2(self, nums: List[int]) -> int:
        '''
        优化 func_1，j 不用每一此都从 0 开始，只需从上一次的位置开始即可
        因为既然上一次之前都到不了上一次之前的位置，那么必然到不了后面的位置，
        没必要再判断一次
        '''
        length = len(nums)
        if length == 1:
            return 0
        dp = [0] * length
        j = 0
        for i in range(1, length):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        return dp[-1]

    def func_3(self, nums: List[int]) -> int:
        '''
        跑通过了，但是快超时了
        执行用时只打败了 5.7% 的用户
        内存消耗打败了 79.87% 的用户
        '''
        length = len(nums)
        if length == 1:
            return 0
        dp = [-1] * length
        dp[0] = 0
        for i in range(0, length):
            for j in range(i + 1, length if i + nums[i] + 1 > length else i + nums[i] + 1):
                if dp[j] == -1:
                    dp[j] = dp[i] + 1
                else:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

    def func_4(self,nums: List[int]) -> int:
        '''
        根据递增特性对 func_3 优化了一下
        执行用时打败了 13.94% 的用户
        内存消耗打败了 68.32% 的用户
        '''
        length = len(nums)
        if length == 1:
            return 0
        dp = [-1] * length
        dp[0] = 0
        for i in range(0, length):
            for j in range(i + 1, length if i + nums[i] + 1 > length else i + nums[i] + 1):
                if dp[j] == -1:
                    dp[j] = dp[i] + 1
                else:
                    continue
                if j == length - 1:
                    return dp[-1]
        return dp[-1]

    def jump(self, nums: List[int]) -> int:
        return self.func_2(nums)
