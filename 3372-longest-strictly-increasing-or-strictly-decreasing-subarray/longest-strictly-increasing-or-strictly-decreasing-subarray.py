class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        inc_len = 1
        desc_len = 1
        max_inc = 1
        max_desc = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_len += 1
            else:
                inc_len = 1
            max_inc = max(max_inc, inc_len)

            if nums[i] < nums[i-1]:
                desc_len += 1
            else:
                desc_len = 1
            max_desc = max(max_desc, desc_len)
        return max(max_inc, max_desc)