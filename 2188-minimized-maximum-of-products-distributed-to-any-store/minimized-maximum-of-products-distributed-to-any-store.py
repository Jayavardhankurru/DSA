class Solution:
    def canDistribute(self, n, quantities, mid):
        stores = 0
        for quantity in quantities:
            stores += math.ceil(quantity / mid)
        if stores <= n:
            return True
        else:
            return False

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        ans = 0
        low = 1
        high = max(quantities)
        while low <= high:
            mid = (low + high) // 2
            if self.canDistribute(n, quantities, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans