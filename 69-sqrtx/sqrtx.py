class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low = 1
        high = x
        res = 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
