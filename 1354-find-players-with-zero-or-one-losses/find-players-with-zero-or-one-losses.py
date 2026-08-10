class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)
        for i, j in matches:
            winners[i] += 1
            losers[j] += 1
        ans1 = []
        ans2 = []
        for num, freq in winners.items():
            if num not in losers:
                ans1.append(num)
        for num, freq in losers.items():
            if freq == 1:
                ans2.append(num)
        ans1.sort()
        ans2.sort()
        return [ans1, ans2]