from typing import List


class Solution:
    def func_1(self, prices: List[int]) -> int:
        '''
        思路：用两个一位数组来表示当天交易结束持有股票和未持有股票两种状态
        none_profit：第 i 天交易结束后未持有股票的最大利润
        hold_profit：第 i 天交易技术后持有股票的最大利润
        第 i 天未持有股票有两种情况：
        1. 前一天也未持有股票，那么最大利润就是前一天未持有的最大利润
        2. 前一天持有股票，那么最大利润就是前一天持有股票的最大利润 + 今天股票的价钱
        第 i 天持有股票有两种情况：
        1. 前一天持有股票，今天没卖，那么最大利润就是前一天持有的最大利润
        2. 前一天未持有股票，根据题意今天是冷却期，所以这种情况就是未持有股票情况 1
           那么我们需要的是前两天的未持有股票的最大收益 - 今天股票的价钱
        注意：利润并不是真正意义的利润，更精确的说：将一开始手里的钱看为 0 ，
        到第 i 天手里的钱相比 0 是多了还是少了。
        执行用时：击败 70.80%
        内存消耗：击败 78.00%
        '''
        days = len(prices)
        if days == 1:
            return 0
        elif days == 2:
            return max(0, prices[1] - prices[0])
        none_profit = [0, max(0, prices[1] - prices[0])]
        hold_profit = [-prices[0], max(-prices[1], -prices[0])]
        for i in range(2, days):
            none_profit.append(
                max(none_profit[i - 1], hold_profit[i - 1] + prices[i]))
            hold_profit.append(
                max(none_profit[i - 2] - prices[i], hold_profit[i - 1]))
        return none_profit[-1]

    def func_2(self, prices: List[int]) -> int:
        '''
        对 func_1 的内存优化
        执行用时：击败 45.80%
        内存消耗：击败 80.19%
        '''
        days = len(prices)
        if days == 1:
            return 0
        elif days == 2:
            return max(0, prices[1] - prices[0])
        none1 = 0
        none2 = max(0, prices[1] - prices[0])
        hold = max(-prices[1], -prices[0])
        for i in range(2, days):
            none_profit = max(none2, hold + prices[i])
            hold_profit = max(none1 - prices[i], hold)
            none1, none2, hold = none2, none_profit, hold_profit
        return none2

    def func_3(self, prices: List[int]) -> int:
        '''
        采用三种状态表示
        执行用时：击败 45.00%
        内存消耗：击败 65.73%
        '''
        days = len(prices)
        if days == 1:
            return 0
        elif days == 2:
            return max(0, prices[1] - prices[0])
        none_profit = [0, max(0, prices[1] - prices[0])]
        hold_profit = [-prices[0], max(-prices[1], -prices[0])]
        cold_profit = [0, 0]
        for i in range(2, days):
            none_profit.append(
                max(none_profit[i - 1], hold_profit[i - 1] + prices[i]))
            hold_profit.append(
                max(hold_profit[i - 1], cold_profit[i - 1] - prices[i]))
            cold_profit.append(none_profit[i - 1])
        return max(cold_profit[i], none_profit[i])

    def func_4(self, prices: List[int]) -> int:
        '''
        对 func_3 的内存优化
        执行用时：击败 96.58%
        内存消耗：击败 80.04%
        '''
        days = len(prices)
        if days == 1:
            return 0
        elif days == 2:
            return max(0, prices[1] - prices[0])
        none_profit = max(0, prices[1] - prices[0])
        hold_profit = max(-prices[1], -prices[0])
        cold_profit = 0
        for i in range(2, days):
            none = max(none_profit, hold_profit + prices[i])
            hold = max(hold_profit, cold_profit - prices[i])
            cold = none_profit
            none_profit, hold_profit, cold_profit = none, hold, cold
        return max(cold_profit, none_profit)

    def maxProfit(self, prices: List[int]) -> int:
        return self.func_4(self, prices)
