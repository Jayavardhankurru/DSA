class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return res
        mpp = defaultdict(int)
        for c in p:
            mpp[c] += 1
        cnt = len(p)
        i = 0
        for j in range(len(s)):
            ch = s[j]
            val = mpp[ch]
            if val > 0:
                cnt -= 1
            mpp[ch] = val - 1
            if j - i + 1 > len(p):
                leftchar = s[i]
                leftval = mpp[leftchar]
                if leftval >= 0:
                    cnt += 1
                mpp[leftchar] = leftval + 1
                i += 1
            if cnt == 0:
                res.append(i)
        return res