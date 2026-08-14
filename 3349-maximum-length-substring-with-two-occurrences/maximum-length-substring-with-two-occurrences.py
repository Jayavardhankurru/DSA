class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = float("-inf")
        mpp = defaultdict(int)
        i = 0
        for j in range(len(s)):
            mpp[s[j]] += 1
            while mpp[s[j]] > 2:
                mpp[s[i]] -= 1
                if mpp[s[i]] == 0:
                    mpp.pop(s[i])
                i += 1
            ans = max(ans, j - i + 1)
        return ans