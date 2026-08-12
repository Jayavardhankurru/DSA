class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_count = defaultdict(int)
        ans = []
        for ball, color in queries:
            if ball in ball_color:
                old_color = ball_color[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    color_count.pop(old_color)
            ball_color[ball] = color
            color_count[color] += 1
            ans.append(len(color_count))
        return ans