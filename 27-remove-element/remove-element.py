class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_index = 0
        for num in nums:
            if num != val:
                nums[valid_index] = num
                valid_index += 1
        return valid_index