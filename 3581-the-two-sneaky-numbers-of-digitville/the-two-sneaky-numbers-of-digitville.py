class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for num, freq in c.items():
            if freq == 2:
                res.append(num)
        return res