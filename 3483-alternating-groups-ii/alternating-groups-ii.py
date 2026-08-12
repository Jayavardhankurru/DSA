class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:(k - 1)])
        cnt = 0
        i = 0
        for j in range(len(colors)):
            if j > 0 and colors[j] == colors[j - 1]:
                i = j
            if j - i + 1 >= k:
                cnt += 1
        return cnt