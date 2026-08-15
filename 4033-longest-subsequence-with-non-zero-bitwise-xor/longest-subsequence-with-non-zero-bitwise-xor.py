class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if n * [0] == nums:
            return 0
        xor = 0
        for num in nums:
            xor = xor ^ num
        if xor != 0:
            return n
        else:
            return n - 1