class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mini = min(nums)
        maxi = max(nums)
        res = (maxi - mini) * k
        return res