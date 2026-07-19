class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            for digit in str(i):
                res.append(int(digit))
        return res