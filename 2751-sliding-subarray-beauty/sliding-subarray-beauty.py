class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = [0] * 51
        ans = []
        i = 0
        for j in range(len(nums)):
            if nums[j] < 0:
                freq[abs(nums[j])] += 1
            if j - i + 1 >= k:
                cnt = 0
                for L in range(50, -1, -1):
                    cnt += freq[L]
                    if cnt >= x:
                        ans.append(-L)
                        break
                if cnt < x:
                    ans.append(0)
                if nums[i] < 0:
                    freq[abs(nums[i])] -= 1
                i += 1
        return ans