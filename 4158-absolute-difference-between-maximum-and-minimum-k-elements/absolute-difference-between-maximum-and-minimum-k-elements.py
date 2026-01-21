class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        sos = sum(arr[:k])
        sol = sum(arr[-k:])
        return sol - sos
        
