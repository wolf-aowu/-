class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        最优子问题就是，到 i 时能够到达的最远距离
        注意：到 i 时需要先判断 i - 1 的最远距离能否达到 i，如果不能直接返回 False
        '''
        length = len(nums)
        if length == 1:
            return True
        before = nums[0]
        for i in range(1, length):
            if before < i:
                return False
            before = max(before, i + nums[i])
        return True
