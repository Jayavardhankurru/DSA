class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_cnt = Counter(s1.split()) + Counter(s2.split())
        return [word for word, frequency in word_cnt.items() if frequency == 1]