class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = 1 << n
        ans = []
        for num in range(0, subsets):
            lst = []
            for i in range(0, n):
                if num & (1<<i):
                    lst.append(nums[i])
            ans.append(lst)
        return ans