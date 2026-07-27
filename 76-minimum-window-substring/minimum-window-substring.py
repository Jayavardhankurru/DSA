class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tMap = defaultdict(int)
        for c in t:
            tMap[c] += 1
        i = 0
        cnt = len(t)
        mini = float("inf")
        ans = ""
        sMap = defaultdict(int)
        for j in range(len(s)):
            sMap[s[j]] += 1
            if s[j] in tMap and sMap[s[j]] <= tMap[s[j]]:
                cnt -= 1
            while cnt == 0:
                if j - i + 1 < mini:
                    mini = j - i + 1
                    ans = s[i:j + 1]
                leftChar = s[i]
                sMap[leftChar] -= 1
                if leftChar in tMap and sMap[leftChar] < tMap[leftChar]:
                    cnt += 1
                i += 1
        return ans
