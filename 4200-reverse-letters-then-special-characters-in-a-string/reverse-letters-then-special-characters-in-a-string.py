class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        special = []
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                special.append(ch)
        letters.reverse()
        special.reverse()
        i = 0
        j = 0
        arr = []
        for ch in s:
            if ch.isalpha():
                arr.append(letters[i])
                i += 1
            else:
                arr.append(special[j])
                j += 1
        return "".join(arr)