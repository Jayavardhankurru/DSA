class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        summ = 0
        odd = 0
        even = 0
        res = 0
        mod = 10 ** 9 + 7
        for num in arr:
            summ += num
            if summ % 2 == 1:
                res += 1 + even
                odd += 1
            else:
                res += odd
                even += 1
        return res % mod

