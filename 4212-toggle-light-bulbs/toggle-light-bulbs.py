class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        s = Counter(bulbs)
        res = []
        for bulb, freq in s.items():
            if freq % 2 == 1:
                res.append(bulb)
        res.sort()
        return res