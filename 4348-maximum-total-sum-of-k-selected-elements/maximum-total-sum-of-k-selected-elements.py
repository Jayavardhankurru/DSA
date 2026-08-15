class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse = True)
        totalSum = 0
        for i in range(k):
            if mul >= 1:
                totalSum += nums[i] * mul
            else:
                totalSum += nums[i]
            mul -= 1
        return totalSum