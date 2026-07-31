class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]
        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i] + suffix[i + 1]
        for i in range(n):
            if i == 0:
                if 0 == suffix[i + 1]:
                    return i
            elif i == n - 1:
                if prefix[i - 1] == 0:
                    return i
            elif prefix[i - 1] == suffix[i + 1]:
                return i
        return -1
