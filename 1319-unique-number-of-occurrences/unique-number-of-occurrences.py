class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = Counter(arr)
        a = []
        for i in s.values():
            if i not in a:
                a.append(i)
            else:
                return False
        return True