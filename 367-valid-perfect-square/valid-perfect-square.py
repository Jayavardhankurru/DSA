class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def feasible(x: int) -> bool:
            return x * x >= num
        left = 1
        right = num
        sol = -1
        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                sol = mid
                right = mid - 1
            else:
                left = mid + 1
        return sol != 0 and sol * sol == num