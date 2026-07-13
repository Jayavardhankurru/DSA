class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        s = Counter(nums)
        for i in s:
            if s[i] == 1 and i + 1 not in s and i - 1 not in s:
                res.append(i)
        return res
