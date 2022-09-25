class Solution:
    def func_1(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(1, rowIndex + 2):
            if i == 1:
                nums = [1]
            elif i == 2:
                nums = [1, 1]
            else:
                nums = [1] * i
                for j in range(1, i - 1):
                    nums[j] = res[i - 2][j - 1] + res[i - 2][j]
            res.append(nums)
        return res[rowIndex]

    def func_2(self, rowIndex: int) -> List[int]:
        '''
        测试了一下这个方法并没有节省空间，官方题解里也没有 python 的代码，也许 python 特殊
        '''
        before = []
        for i in range(1, rowIndex + 2):
            if i == 1:
                nums = [1]
            elif i == 2:
                nums = [1, 1]
                before = nums
            else:
                nums = [1] * i
                for j in range(1, i - 1):
                    nums[j] = before[j - 1] + before[j]
                before = nums
            if i == rowIndex + 1:
                return nums

    def getRow(self, rowIndex: int) -> List[int]:
        return self.func_1(rowIndex)
        