class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        greatest = float("-inf")
        smallest = float("inf")
        left = 0
        right = 0
        for i in range(len(nums)):
            if nums[i] >= greatest:
                greatest = nums[i]
            else:
                right = i
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= smallest:
                smallest = nums[i]
            else:
                left = i
        if left != 0 or right != 0:
            return right - left + 1
        else:
            return 0