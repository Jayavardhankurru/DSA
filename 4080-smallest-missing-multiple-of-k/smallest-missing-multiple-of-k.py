class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        curr = k
        while curr in s:
            curr += k
        return curr