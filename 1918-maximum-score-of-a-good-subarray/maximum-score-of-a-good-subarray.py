class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        score = 0
        currMin = nums[k]
        maxi = currMin
        while i > 0 or j < len(nums) - 1:
            if i == 0:
                j += 1
                currMin = min(currMin, nums[j])
                score = currMin * (j - i + 1)

            elif j == len(nums) - 1:
                i -= 1
                currMin = min(currMin, nums[i])
                score = currMin * (j - i + 1)

            elif nums[i - 1] > nums[j + 1]:
                i  -= 1
                currMin = min(currMin, nums[i])
                score = currMin * (j - i + 1)

            else:
                j += 1
                currMin =  min(currMin, nums[j])
                score = currMin * (j - i + 1)
                
            maxi = max(maxi, score)
        return maxi