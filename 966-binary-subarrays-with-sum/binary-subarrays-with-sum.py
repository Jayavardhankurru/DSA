class Solution:
    def atmost(self, nums, goal):
        if goal < 0:
            return 0
        l = 0
        n = len(nums)
        cnt = 0
        summ = 0
        for r in range(n):
            summ += nums[r]
            while summ > goal:
                summ -= nums[l]
                l += 1
            cnt += (r - l) + 1
        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atmost(nums, goal) - self.atmost(nums, goal - 1)