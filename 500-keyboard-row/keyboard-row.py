class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        first =  set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        for word in words:
            word_chars = set(word.lower())
            if word_chars <= first or word_chars <= second or word_chars <=third:
                result.append(word)
        return result