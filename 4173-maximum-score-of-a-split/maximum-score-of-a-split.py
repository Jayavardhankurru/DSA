class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]
        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])
        maxi = float("-inf")
        for i in range(n - 1):
            score = prefix[i] - suffix[i + 1]
            maxi = max(maxi, score)
        return maxi