class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mpp = defaultdict(int)
        mpp[0] = 1
        cnt = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            target = summ % k
            if target in mpp:
                cnt += mpp[target]
            mpp[target] += 1
        return cnt