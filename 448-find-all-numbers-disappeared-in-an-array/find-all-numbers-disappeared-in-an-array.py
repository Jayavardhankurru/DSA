class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set(nums)
        n = len(nums)
        numbers = [numbers for numbers in range(1, n + 1) if numbers not in ans]
        return numbers