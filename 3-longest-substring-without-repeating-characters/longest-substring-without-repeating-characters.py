class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        setx = set()
        max_length = float('-inf')
        for r in range(len(s)):
            if s[r] in setx:
                while l < r and s[r] in setx:
                    setx.remove(s[l])
                    l += 1
            setx.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length