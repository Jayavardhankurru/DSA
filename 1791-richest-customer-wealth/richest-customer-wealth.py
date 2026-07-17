class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for i in accounts:
            summ = sum(i)
            maxi = max(maxi, summ)
        return maxi
