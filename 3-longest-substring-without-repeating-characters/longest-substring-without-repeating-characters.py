class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = [-1] * 256
        l = 0
        r = 0
        n = len(s)
        length = 0
        while r < n:
            if mpp[ord(s[r])] != -1:
                l = max(mpp[ord(s[r])] + 1, l)
            mpp[ord(s[r])] = r
            length = max(length, r - l + 1)
            r += 1
        return length