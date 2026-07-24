class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        i = 0
        cnt = 0
        product = 1
        for j in range(len(nums)):
            product *= nums[j]
            while product >= k:
                product //= nums[i]
                i += 1
            cnt += j - i + 1
        return cnt