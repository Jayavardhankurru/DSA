class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mpp = set()
        for i in range(len(nums)):
            if nums[i] in mpp:
                return True
            mpp.add(nums[i])
        return False