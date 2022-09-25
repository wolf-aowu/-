class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            if i == 1:
                nums = [1]
            elif i == 2:
                nums = [1, 1]
            else:
                nums = [1] * i
                for j in range(1, i - 1):
                    nums[j] = res[i - 2][j - 1] + res[i - 2][j]
            res.append(nums)
        return res
