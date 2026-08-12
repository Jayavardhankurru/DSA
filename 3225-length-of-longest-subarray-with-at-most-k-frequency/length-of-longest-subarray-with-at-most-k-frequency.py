class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        maxi = float("-inf")
        mpp = defaultdict(int)
        for j in range(len(nums)):
            mpp[nums[j]] += 1
            if mpp[nums[j]] <= k:
                maxi = max(maxi, j - i + 1)
            else:
                while mpp[nums[j]] > k:
                    mpp[nums[i]] -= 1
                    if mpp[nums[i]] == 0:
                        mpp.pop(nums[i])
                    i += 1
        return maxi