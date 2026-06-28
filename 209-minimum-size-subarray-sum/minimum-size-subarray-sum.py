class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        mini = float("inf")
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                mini = min(mini, (r - l) + 1)
                summ -= nums[l]
                l += 1
        return 0 if mini == float("inf") else mini