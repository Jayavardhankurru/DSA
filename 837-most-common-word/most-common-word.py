class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)
        word_count = Counter(re.findall(r'[a-z]+', paragraph.lower()))
        for word, count in word_count.most_common():
            if word not in banned_words:
                return word