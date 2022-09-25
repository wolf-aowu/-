class Solution:
    def func_1(self, prices: List[int]) -> int:
        '''
        这一题就是求数组的最大和，不再要求其连续性
        该方法为 动态规划，dp 代表到 i 的最大和，可以不包含 i
        执行用时：打败了 27.36%
        内存消耗：打败了 87.71%
        '''
        days = len(prices)
        if days == 1:
            return 0
        gaps = []
        for i in range(1, days):
            gaps.append(prices[i] - prices[i - 1])
        profit = 0
        for i in range(days - 1):
            profit = max(profit + gaps[i], profit)
        return profit

    def func_2(self, prices: List[int]) -> int:
        '''
        这道题可以看成所有正利润的和
        执行用时：打败了 75.35%
        内存消耗：打败了 77.69%
        '''
        days = len(prices)
        if days == 1:
            return 0
        profit = 0
        for i in range(1, days):
            profit += max(0, prices[i] - prices[i - 1])
        return profit

    def func_3(self, prices: List[int]) -> int:
        '''
        这题还可以将一天分成两种情况：
        1. 今天持有股票，
           那么它的前提条件是前一天持有股票或者前一天未持有股票但今天买入了
        2. 今天没有股票，
           那么它的前提条件是前一天未持有股票或者前一天持有股票但今天卖出了
        把这两种情况都算出来，就不会有漏掉的解了
        使用二维数组来存储这两种情况，dp[i][j]
        j 代表第 i 天交易完后的状态是没有股票还是持有股票
        dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润
        dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润
        所以，dp[i][0] = max(dp[i - 1][0],dp[i - 1][1] + price[i])
        或者，dp[i][1] = max(dp[i - 1][1],dp[i - 1][0] - price[i])
        最后一定是手里没有股票的利润最大。
        因为如果手里有股票那么在买股票的那一天的利润一定大于买后的，毕竟天下不可能有免费的午餐，白送钱给你。
        执行用时：打败了 18.13%
        内存消耗：打败了 8.37%
        '''
        days = len(prices)
        if days == 1:
            return 0
        dp = [[0] * 2 for i in range(days)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, days):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[days - 1][0]

    def func_4(self, prices: List[int]) -> int:
        '''
        对 func_3 的内存优化，因为后一状态只涉及前一状态
        执行用时：打败了 89.50%
        内存消耗：打败了 23.06%
        '''
        days = len(prices)
        if days == 1:
            return 0
        dp = [[0] * 2 for i in range(days)]
        none_before = 0
        hold_before = -prices[0]
        for i in range(1, days):
            none = max(none_before, hold_before + prices[i])
            hold = max(hold_before, none_before - prices[i])
            none_before = none
            hold_before = hold
        return none_before

    def maxProfit(self, prices: List[int]) -> int:
        '''
        使用动态规划的本质是降低算法时间复杂度和空间复杂度，
        如果暴力本身时间复杂度和空间复杂度不高，可以不用特意使用动态规划
        个人感觉 LeetCode 上的执行用时和内存消耗只能作为参考，因为相同代码多次运行结果相差会很大
        '''
        return self.func_4(self, prices)
