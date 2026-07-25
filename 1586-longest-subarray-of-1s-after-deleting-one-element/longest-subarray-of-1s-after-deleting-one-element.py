class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size = 0
        max_size = 0
        zeros = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                size += 1
            else:
                zeros += 1
            while zeros > 1:
                if nums[i] == 0:
                    zeros -= 1
                else:
                    size -= 1
                i += 1
            max_size = max(size, max_size)
        if max_size == len(nums):
            return max_size - 1
        else:
            return max_size