class Solution:
    def canDivide(self, nums, maxOperations, mid):
        bags = 0
        for num in nums:
            bags += (num - 1 ) // mid
        if bags <= maxOperations:
            return True
        else:
            return False

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        ans = 0
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.canDivide(nums, maxOperations, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans