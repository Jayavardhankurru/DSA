class Solution:
    def checkValidString(self, s: str) -> bool:
        minn = 0
        maxx = 0
        for c in s:
            if c == '(':
                minn += 1
                maxx += 1
            elif c == ')':
                minn -= 1
                maxx -= 1
            else:
                minn -= 1
                maxx += 1
            if (minn < 0):
                minn = 0
            if (maxx < 0):
                return False
        return minn == 0