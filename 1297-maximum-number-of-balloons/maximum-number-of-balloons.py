class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_cnt = Counter(text)
        char_cnt['l'] //= 2
        char_cnt['o'] //= 2
        return min(char_cnt[c] for c in 'balon')