class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        x = {}
        for i in range(len(s)):
            if s[i] not in x:
                x[s[i]] = [i]
            else:
                x[s[i]].append(i)
        
        maxi = -1
        for num, freq in x.items():
            if len(freq) >= 2:
                maxi = max(maxi, freq[-1] - freq[0] - 1)
        return maxi