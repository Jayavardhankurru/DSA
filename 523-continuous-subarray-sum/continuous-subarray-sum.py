class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        summ = 0
        mpp = defaultdict(int)
        mpp[0] = -1
        for i in range(len(nums)):
            summ += nums[i]
            target = summ % k
            if target in mpp:
                if i - mpp[target] >= 2:
                    return True
            else:
                mpp[target] = i
        return False