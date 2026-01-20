class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        i = 0
        res = []
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            size = j - i
            if size >= 3:
                res.append([i, j - 1])
            i = j
        return res