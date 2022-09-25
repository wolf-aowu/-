from cmath import cos


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost) + 1
        if top == 0 or top == 1:
            return 0
        dp = [0, 0]
        for i in range(2, top):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))
        return dp[top - 1]
