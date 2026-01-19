class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], i - prev)
        nex = float('inf')
        for i in range(n-1, -1, -1):
            if s[i] == c:
                nex = i
            ans[i] = min(ans[i], nex - i)
        return ans