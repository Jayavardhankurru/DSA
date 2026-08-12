class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        cnt = 0
        for i in range(n):
            left = colors[(i - 1) % n]
            middle = colors[i]
            right = colors[(i + 1) % n]
            if left != middle and middle != right:
                cnt += 1
        return cnt