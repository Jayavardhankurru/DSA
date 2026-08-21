class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        a = []
        for x in coins:
            if all(x % c for c in a):
                a.append(x)
        def check(m):
            total = 0
            for x in range(1, len(a)  + 1):
                for c in combinations(a, x):
                    total += m // lcm(*c) * pow(-1, x + 1)
            return total >= k
        return bisect_left(range(k * a[0] + 1), True, lo = 1, key = check)