class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = [0] *  len(capacity)
        for i in range(len(capacity)):
            diff[i] = capacity[i] - rocks[i]
        diff.sort()
        full = 0
        for need in diff:
            if need <= additionalRocks:
                additionalRocks -= need
                full += 1
            else:
                break
        return full