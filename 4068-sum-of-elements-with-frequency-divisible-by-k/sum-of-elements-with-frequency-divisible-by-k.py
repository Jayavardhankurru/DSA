class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        s =  Counter(nums)
        total = 0
        for key, v in s.items():
            if v % k == 0:
                total += key * v
        return total
