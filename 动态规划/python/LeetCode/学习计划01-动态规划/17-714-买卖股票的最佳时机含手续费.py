class Solution:
    def func_1(self, prices: List[int], fee: int) -> int:
        '''
        执行用时：击败了 66.97%
        内存消耗：击败了 63.03%
        '''
        length = len(prices)
        if length == 1:
            return 0
        none = 0
        hold = -prices[0]
        for i in range(1, length):
            temp = max(none, hold + prices[i] - fee)
            hold = max(hold, none - prices[i])
            none = temp
        return none

    def func_2(self, prices: List[int], fee: int) -> int:
        '''
        内存优化不用使用 3 个变量
        执行用时：击败了 74.33%
        内存消耗：击败了 55.85%
        '''
        length = len(prices)
        if length == 1:
            return 0
        none = 0
        hold = -prices[0]
        for i in range(1, length):
            none, hold = max(none, hold + prices[i] - fee), \
                max(hold, none - prices[i])
        return none

    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.func_2(self, prices, fee)
