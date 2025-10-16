from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = defaultdict(int)
        mapp[0] = 1
        prefix_sum = 0
        cnt = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remove = prefix_sum - k
            cnt += mapp[remove]
            mapp[prefix_sum] += 1
        return cnt
