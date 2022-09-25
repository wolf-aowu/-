class Solution:
    def func_1(self, values: List[int]) -> int:
        '''
        用的是 动态规划
        题目中给出的一对景点组成的观光组合得分是：values[i] + values[j] + i - j
        我们可以将公式变一下形：values[i] + i + values[j] - j
        这样 i 和 j 可以分开看，互不影响
        可以定义两个 dp
        dp1 为 到 i 时 values[i] + i 的最大得分
        dp2 为 最大一对观光组合得分
        执行用时：击败 56.87%
        内存消耗：击败 19.43%
        '''
        count = len(values)
        dp1 = values[0] + 0
        dp2 = 0
        for i in range(1, count):
            temp = max(dp1, values[i] + i)
            dp2 = max(dp2, dp1 + values[i] - i)
            dp1 = temp
        return dp2

    def func_2(self, values: List[int]) -> int:
        '''
        使用 mx 记录 values[i] + i 的最大值
        再使用 ans 记录 一对景点组成的观光组合得分的最大值
        然后判断 mx + values[i] - i > ans 如果是更新 ans
        然后判断 values[i] + i > mx 如果是更新 mx
        执行用时：击败 65.17%
        内存消耗：击败 77.01%
        与 func_1 代码其实是一样的，func_1 中的 dp2 的值并不影响 dp1 的值，
        所以 dp2 可以提前算，这样就不需要 temp 了
        '''
        count = len(values)
        ans = 0
        mx = values[0] + 0
        for i in range(1, count):
            ans = max(mx + values[i] - i, ans)
            mx = max(mx, values[i] + i)
        return ans

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        return self.func_2(self, values)
