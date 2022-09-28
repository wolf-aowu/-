from cgitb import reset
from operator import le


class Solution:
    def func_1(self, height: List[int]) -> int:
        '''
        思路：想要接住雨水就要符合两边高，中间低的条件
        对于 i 处，我们就需要知道它的左右两边最高的高度，
        然后比较左右两边的最高高度的得到高度的最小值就是 i 处可以接住的水了
        优化：树状图的两端是接不住水的
        '''
        length = len(height)
        if length < 3:
            return 0
        # 从左边开始记录
        left = [0, height[0]]
        # 从右边开始记录
        right = [0, height[-1]]
        res = 0
        for i in range(2, length):
            left.append(max(height[i - 1], left[i - 1]))
            right.append(max(height[-i], right[i - 1]))
        for i in range(1, length - 1):
            res += max(0, min(left[i], right[-i - 1]) - height[i])
        return res

    def func_2(self, height: List[int]) -> int:
        '''
        提前开辟需要的数组空间，不使用 append 函数添加元素，
        内存消耗明显提升，执行用时也有提升
        func_1 内存消耗平均 16.6 MB，func_2 内存消耗平均 16.5 MB
        官方代码，执行用时和内存消耗与 func_1 差不多
        '''
        length = len(height)
        if length < 3:
            return 0
        # 从左边开始记录
        left = [0, height[0]] + [0] * (length - 2)
        # 从右边开始记录
        right = [0, height[-1]] + [0] * (length - 2)
        res = 0
        for i in range(2, length):
            left[i] = max(height[i - 1], left[i - 1])
            right[i] = max(height[-i], right[i - 1])
        for i in range(1, length - 1):
            res += max(0, min(left[i], right[-i - 1]) - height[i])
        return res

    def trap(self, height: List[int]) -> int:
        return self.func_2(height)
