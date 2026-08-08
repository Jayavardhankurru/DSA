class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mini = maxi = nums[0]
        minInd = maxInd = 0
        for ind, val in enumerate(nums):
            if val < mini:
                mini = val
                minInd = ind
            elif val > maxi:
                maxi = val
                maxInd = ind
        deleteFromFront = max(minInd, maxInd) + 1
        deleteFromBack = n - min(minInd, maxInd)
        deleteFromBoth = (min(minInd, maxInd) + 1) + (n - max(minInd, maxInd))
        return min(deleteFromFront, deleteFromBack, deleteFromBoth)