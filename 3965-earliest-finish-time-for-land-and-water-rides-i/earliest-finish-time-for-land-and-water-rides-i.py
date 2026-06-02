class Solution:
    def cal_finish_time(self, a1, b1, a2, b2):
        min_first_ride = min(a + b for a, b in zip(a1, b1))
        min_total_time = min(max(min_first_ride, a) + b for a, b in zip(a2, b2))
        return min_total_time

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_water = self.cal_finish_time(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = self.cal_finish_time(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_water, water_land)
