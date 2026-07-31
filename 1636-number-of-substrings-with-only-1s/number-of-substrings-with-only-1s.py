class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        total = 0
        mod = 10 ** 9 + 7
        for i in s:
            if i == '1':
                cnt += 1
            else:
                cnt = 0
            total = (total + cnt) % mod
        return total