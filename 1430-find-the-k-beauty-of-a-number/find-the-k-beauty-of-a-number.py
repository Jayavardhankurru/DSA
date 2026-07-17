class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        cnt = 0
        for i in range(len(s) - k + 1):
            val = int(s[i:i + k])
            if val != 0 and num % val == 0:
                cnt += 1
        return cnt