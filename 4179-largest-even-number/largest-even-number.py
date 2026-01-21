class Solution:
    def largestEven(self, s: str) -> str:
        while len(s) > 0 and s[-1] == '1':
            s = s[:-1]
        return s