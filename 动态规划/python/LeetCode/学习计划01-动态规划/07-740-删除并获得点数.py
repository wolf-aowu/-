from typing import List


class Solution:
    def func_1(self, nums: List[int]) -> int:
        '''
        根据题意可知，删除一个数字后，与它相等的数字都不会受影响，都可以删除，
        这样才能尽可能获取更多的点数，所以可以统计 nums 数组中每种相同数字的和，
        然后就可以将其看成 打家劫舍 类型的题目
        在代码前半部分先处理边界情况，排除 nums 是空的或只有一个数的情况后，
        新建的 numCount 的长度一定大于等于 2，所以不许要再次处理边界情况了
        '''
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        maxNum = max(nums)
        numCount = [0] * (maxNum + 1)
        for num in nums:
            numCount[num] += num
        first = numCount[0]
        second = max(numCount[0], numCount[1])
        for i in range(2, maxNum + 1):
            res = max(first + numCount[i], second)
            first, second = second, res
        return second

    def func_2(self, nums: List[int]) -> int:
        '''
        对 func_1 的优化，打家劫舍那一部分直接从 nums 的最小数字开始遍历
        从最小的那个数开始遍历会有一个坑，例如 [1,1,1] 会导致 numCount 为 [0,3]，
        此时从 minNum = 1 开始遍历，second = max(numCount[minNum],numCount[minNum]) 就会越界
        所以，需要判断 maxNum 和 minNum 是不是同一个数字，如果是直接返回 numCount[minNum]
        '''
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        maxNum = max(nums)
        minNum = min(nums)
        numCount = [0] * (maxNum + 1)
        for num in nums:
            numCount[num] += num
        length = len(numCount)
        if maxNum == minNum:
            return numCount[minNum]
        first = numCount[minNum]
        second = max(numCount[minNum], numCount[minNum + 1])
        for i in range(minNum + 2, maxNum + 1):
            res = max(first + numCount[i], second)
            first, second = second, res
        return second

    def deleteAndEarn(self, nums: List[int]) -> int:
        return self.func_2(nums)
