class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = 0
        right_sum = 0
        max_sum = 0
        n = len(cardPoints)
        left_sum = sum(cardPoints[:k])
        max_sum = left_sum
        right = n - 1
        for i in range(k-1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right]
            right -= 1
            max_sum = max(max_sum, left_sum + right_sum)
        return max_sum