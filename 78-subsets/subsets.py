class Solution:
    def func(self, ind, nums, res, subset):
        if ind >= len(nums):
            res.append(list(subset))
            return
        subset.append(nums[ind])
        self.func(ind + 1, nums, res, subset)
        subset.pop()
        self.func(ind + 1, nums, res, subset)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        self.func(0, nums, res, subset)
        return res