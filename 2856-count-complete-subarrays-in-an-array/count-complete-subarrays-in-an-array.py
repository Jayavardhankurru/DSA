class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        cnt = 0
        mpp = defaultdict(int)
        i = 0
        for j in range(len(nums)):
            mpp[nums[j]] += 1
            while len(mpp) == k:
                cnt += len(nums) - j
                mpp[nums[i]] -= 1
                if mpp[nums[i]] == 0:
                    mpp.pop(nums[i])
                i += 1
        return cnt