class Solution:
    def canTravel(self, time, totalTrips, mid):
        trips = 0
        for i in time:
            trips += (mid // i)
        if trips >= totalTrips:
            return True
        else:
            return False

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        ans = 0
        low = 1
        high = min(time) * totalTrips
        while low <= high:
            mid = (low + high) // 2
            if self.canTravel(time, totalTrips, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans