class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        maxi = float("-inf")
        summ = 0
        for j in range(len(nums)):
            summ += nums[j]
            if j - i + 1 == k:
                average = summ / k
                maxi = max(maxi, average)
                summ -= nums[i]
                i += 1
        return maxi