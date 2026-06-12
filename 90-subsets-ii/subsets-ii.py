class Solution:
    def func(self, ind, nums, res, subset):
        res.append(list(subset))
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.func(i + 1, nums, res, subset)
            subset.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        self.func(0, nums, res, subset)
        return res