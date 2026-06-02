class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i = 0
        j = len(plants) - 1
        a = capacityA
        b = capacityB
        refill = 0
        while i < j:
            if plants[i] > a:
                refill += 1
                a = capacityA
            a -= plants[i]
            i += 1
            if plants[j] > b:
                refill += 1
                b = capacityB
            b -= plants[j]
            j -= 1
        if i == j:
            if max(a, b) < plants[i]:
                refill += 1
        return refill

                    