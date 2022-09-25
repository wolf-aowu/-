class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 2] + dp[i - 1])
        return dp[n]
