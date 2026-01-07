class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        allowed = n / 2
        unique = len(set(candyType))
        return int(min(allowed, unique))