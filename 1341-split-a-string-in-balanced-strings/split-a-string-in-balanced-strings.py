class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0
        for i in s:
            if i == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                ans += 1
        return ans