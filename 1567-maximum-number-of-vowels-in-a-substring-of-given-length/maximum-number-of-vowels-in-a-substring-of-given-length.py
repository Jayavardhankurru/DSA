class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxi = float("-inf")
        i = 0
        vowels = 'aeiou'
        cnt = 0
        for j in range(len(s)):
            if s[j] in vowels:
                cnt += 1
            if k == j - i + 1:
                maxi = max(maxi, cnt)
                if s[i] in vowels:
                    cnt -= 1
                i += 1
        return maxi