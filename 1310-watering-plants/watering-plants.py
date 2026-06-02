class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can_capacity = capacity
        steps = 0
        for i in range(len(plants)):
            if plants[i] <= can_capacity:
                can_capacity -= plants[i]
                steps += 1
            else:
                steps += i + (i + 1)
                can_capacity = capacity
                can_capacity -= plants[i]
        return steps