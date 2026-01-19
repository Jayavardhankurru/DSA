class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        result = []
        for i, word in enumerate(sentence.split()):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += 'ma'
            word += 'a' * (i + 1)
            result.append(word)
        return ' '.join(result)