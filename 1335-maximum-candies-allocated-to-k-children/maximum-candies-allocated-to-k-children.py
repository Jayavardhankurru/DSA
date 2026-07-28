class Solution:
    def giveCandies(self, candies, k, mid):
        children = 0
        for candie in candies:
            children += candie // mid
        return children >= k


    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        ans = 0
        low = 1
        high = max(candies)
        while low <= high:
            mid = (low + high) // 2
            if self.giveCandies(candies, k, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans