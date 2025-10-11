class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
                flag = True
                count += 1
            elif flag == True:
                return count
        return count