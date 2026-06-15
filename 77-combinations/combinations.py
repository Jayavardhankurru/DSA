class Solution:
    def backTrack(self, start, res, comb, n, k):
        if len(comb) == k:
            res.append(comb.copy())
            return
        for i in range(start, n + 1):
            comb.append(i)
            self.backTrack(i + 1, res, comb, n, k)
            comb.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []
        self.backTrack(1, res, comb, n, k)
        return res