class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen = [-1] * 3
        cnt = 0
        for i in range(len(s)):
            lastseen[ord(s[i]) - ord('a')] = i
            cnt = cnt + (1 + min(lastseen[0], lastseen[1], lastseen[2]))
        return cnt