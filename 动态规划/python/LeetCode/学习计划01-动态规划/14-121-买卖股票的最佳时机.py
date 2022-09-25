class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        可以算出每一天与前一天的价格差
        股票从某一天买入到卖出所得的钱，就是把期间每一天的差价加起来的钱
        所以这一题就可以看成求差价的最大子数组和
        '''
        days = len(prices)
        if days == 1:
            return 0
        gaps = []
        for i in range(1, days):
            gaps.append(prices[i] - prices[i - 1])
        profit = [gaps[0]]
        for i in range(1, days - 1):
            profit.append(max(profit[i - 1] + gaps[i], gaps[i]))
        return max(profit) if max(profit) > 0 else 0
