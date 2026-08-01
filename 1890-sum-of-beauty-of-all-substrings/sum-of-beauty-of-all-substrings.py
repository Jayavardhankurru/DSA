class Solution:
    def beautySum(self, s: str) -> int:
        beauty = 0
        for i in range(len(s)):
            mpp = defaultdict(int)
            for j in range(i, len(s)):
                mpp[s[j]] += 1
                maxi = float('-inf')
                mini = float('inf')
                for num, freq in mpp.items():
                    maxi = max(maxi, freq)
                    mini = min(mini, freq)
                beauty += (maxi - mini)
        return beauty