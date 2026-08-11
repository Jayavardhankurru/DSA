class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seen = set(nums)
        summ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                summ += nums[i]
            else:
                break
        while summ in seen:
            summ += 1
        return summ