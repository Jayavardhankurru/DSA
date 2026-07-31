class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mpp = defaultdict(int)
        maxi = 0
        i = 0
        summ = 0
        for j in range(len(nums)):
            summ += nums[j]
            mpp[nums[j]] += 1
            while mpp[nums[j]] > 1:
                summ -= nums[i]
                mpp[nums[i]] -= 1
                if mpp[nums[i]] == 0:
                    mpp.pop(nums[i])
                i += 1
            maxi = max(maxi, summ)
        return maxi