class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        j = len(s) - 1
        while j >= 0 and s[j] in "aeiou":
            j -= 1
        return s[:j + 1]