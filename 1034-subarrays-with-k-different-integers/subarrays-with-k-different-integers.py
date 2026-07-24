class Solution:
    def goodArray(self, nums, k):
        cnt = 0
        i = 0
        mpp = defaultdict(int)
        for j in range(len(nums)):
            mpp[nums[j]] += 1
            while len(mpp) > k:
                mpp[nums[i]] -= 1
                if mpp[nums[i]] == 0:
                    mpp.pop(nums[i])
                i += 1
            cnt += j - i + 1
        return cnt

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
         return self.goodArray(nums, k) - self.goodArray(nums, k - 1)
        