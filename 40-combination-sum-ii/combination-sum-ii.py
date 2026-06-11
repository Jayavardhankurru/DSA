class Solution:
    def func(self, ind, target, arr, ans, ds):
        if target == 0:
            ans.append(list(ds))
            return
        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i - 1]:
                continue
            if arr[i] > target:
                break
            ds.append(arr[i])
            self.func(i + 1, target - arr[i], arr, ans, ds)
            ds.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        ds = []
        self.func(0, target, candidates, ans, ds)
        return ans