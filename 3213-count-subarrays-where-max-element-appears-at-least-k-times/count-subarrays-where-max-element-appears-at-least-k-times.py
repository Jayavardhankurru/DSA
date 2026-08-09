class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        maxi = max(nums)
        i = 0
        maxiCnt = 0
        for j in range(len(nums)):
            if nums[j] == maxi:
                maxiCnt += 1
            while maxiCnt >= k:
                if nums[i] == maxi:
                    maxiCnt -= 1
                i += 1
            cnt += i
        return cnt
