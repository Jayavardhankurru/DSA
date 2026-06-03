class Solution:
    def calFinishTime(self, a1, b1, a2, b2):
        minFirstRide = min(a + b for a, b in zip(a1, b1))
        minFinishTime = min(max(minFirstRide, a) + b for a, b in zip(a2, b2))
        return minFinishTime

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        landWater = self.calFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
        waterLand = self.calFinishTime(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(landWater, waterLand)