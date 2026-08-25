class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        res = 0
        maxi =  0
        for num in nums:
            res += maxi
            maxi = max(maxi, num)
        return res