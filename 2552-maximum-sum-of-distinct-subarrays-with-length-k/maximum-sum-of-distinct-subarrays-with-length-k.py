class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mpp = defaultdict(int)
        summ = 0
        j = 0
        maxi = 0
        for i in range(len(nums)):
            mpp[nums[i]] += 1
            summ += nums[i]
            if (i - j + 1) == k:
                if len(mpp) == k:
                    maxi = max(summ, maxi)
                summ -= nums[j]
                mpp[nums[j]] -= 1
                if mpp[nums[j]] == 0:
                    mpp.pop(nums[j])
                j += 1
        return maxi
