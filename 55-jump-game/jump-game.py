class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxind = 0 
        n = len(nums)
        for i in range(n):
            if  i > maxind:
                return False
            maxind = max(maxind, i + nums[i])
        return True