class Solution:
    def placeBalls(self, position, mid, m):
        balls = 1
        last = position[0]
        for i in range(1, len(position)):
            if abs(last - position[i]) >= mid:
                balls += 1
                last = position[i]
        if balls >= m:
            return True
        else:
            return False

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        ans = 0
        low = 1
        high = position[n - 1] - position[0]
        while low <= high:
            mid = (low + high) // 2
            if self.placeBalls(position, mid, m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
