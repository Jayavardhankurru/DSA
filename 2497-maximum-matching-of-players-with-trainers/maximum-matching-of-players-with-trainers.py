class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        cnt = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
                j += 1
                cnt += 1
            else:
                j += 1
        return cnt