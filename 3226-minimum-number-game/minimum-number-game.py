class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        arr = []
        for i in range(len(nums) // 2):
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(alice)
        return arr