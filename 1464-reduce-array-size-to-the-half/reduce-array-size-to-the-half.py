class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        frequencies = list(cnt.values())
        frequencies.sort()
        ans = 0
        removed = 0
        half = len(arr) // 2
        while removed < half:
            ans +=  1
            removed += frequencies.pop()
        return ans