class Solution:
    def func(self, ind, target, candidates, ans, ds):
        if ind == len(candidates):
            if target == 0:
                ans.append(list(ds))
            return 
        if candidates[ind] <= target:
            ds.append(candidates[ind])
            self.func(ind, target - candidates[ind], candidates, ans, ds)
            ds.pop()
        self.func(ind + 1, target, candidates, ans, ds)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds =  []
        self.func(0, target, candidates, ans, ds)
        return ans