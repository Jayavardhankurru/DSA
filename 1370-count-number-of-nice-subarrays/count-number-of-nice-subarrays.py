class Solution:
    def atmost(self, nums, k):
        if k < 0:
            return 0
        l = 0
        summ = 0
        cnt = 0
        n = len(nums)
        for r in range(n):
            summ += nums[r] % 2
            while summ > k:
                summ -= nums[l] % 2
                l += 1
            cnt += (r - l) + 1
        return cnt

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k - 1)