class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = min(nums[i], prefix[i - 1])
        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])
        summ = float("inf")
        for i in range(1, n - 1):
            min_Left = prefix[i - 1]
            min_Right = suffix[i + 1]
            if min_Left < nums[i] > min_Right:
                summ = min(summ, min_Left + nums[i] + min_Right)
        return -1 if summ == float("inf") else summ