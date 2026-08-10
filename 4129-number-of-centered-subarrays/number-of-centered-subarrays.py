class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            mpp = defaultdict(int)
            summ = 0
            for j in range(i, len(nums)):
                mpp[nums[j]] += 1
                summ += nums[j]
                if summ in mpp:
                    cnt += 1
        return cnt