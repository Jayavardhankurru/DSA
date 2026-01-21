class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        n = len(s)
        score = 0
        for ch in s:
            if ch.isalpha():
                if ch in 'aeiou':
                    v += 1
                else:
                    c += 1
        if c > 0:
            score = v // c
        else:
            score = 0
        return score