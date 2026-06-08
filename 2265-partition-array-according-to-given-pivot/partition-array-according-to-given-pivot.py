class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        pivots = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                pivots.append(num)
        return less + pivots + greater