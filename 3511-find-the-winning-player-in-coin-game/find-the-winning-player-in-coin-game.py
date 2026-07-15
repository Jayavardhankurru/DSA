class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        cnt = 0
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            cnt += 1
        if cnt % 2 == 0:
            return "Bob"
        else:
            return "Alice"