class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_cnt = Counter(chars)
        length = 0
        for word in words:
            word_char_cnt = Counter(word)
            if all(char_cnt[char] >= cnt for char, cnt in word_char_cnt.items()):
                length += len(word)
        return length