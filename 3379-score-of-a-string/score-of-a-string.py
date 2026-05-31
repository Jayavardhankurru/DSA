class Solution:
    def scoreOfString(self, s: str) -> int:
        val = 0
        n = len(s)
        for i in range(n - 1):
                val += abs(ord(s[i]) - ord(s[i + 1]))
        return val