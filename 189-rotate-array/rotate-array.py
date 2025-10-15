class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1
        l, r = 0, k - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1
        l, r = k, len(nums) - 1
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1
        return nums