class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        cnt = 0
        while ans > 0:
            if ans % 2 == 1:
                cnt += 1
            ans = ans // 2
        return cnt