class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
                if cnt > 1:
                    res.append(char)
            else:
                cnt -= 1
                if cnt > 0:
                    res.append(char)
        return ''.join(res)