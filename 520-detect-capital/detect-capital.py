class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = sum(1 for char in word if char.isupper())
        if (count == 0) or (count == len(word)) or (count == 1 and word[0].isupper()):
            return True 
        else:
            return False