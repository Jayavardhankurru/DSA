class Solution:
    def isPalin(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def func(i):
            if i >= len(s):
                res.append(path.copy())
                return
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    path.append(s[i:j+1])
                    func(j + 1)
                    path.pop()
        func(0)
        return res