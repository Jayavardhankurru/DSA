class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [{} for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1, arr)

    def build(self, node, start, end, arr):
        if start == end:
            self.tree[node][arr[start]] = 1 
            return
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid, arr)
        self.build(2 * node + 2, mid + 1, end, arr)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def merge(self, left, right):
        d = left.copy()
        for key in right:
            d[key] = d.get(key, 0) + right[key]
        return d

    def _query(self, node, start, end, left, right, val):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node].get(val, 0)
        mid = (start + end) // 2
        return self._query(2 * node + 1, start, mid, left, right, val) + self._query(2 * node + 2, mid + 1, end, left, right, val)

    def query(self, left: int, right: int, value: int) -> int:
        
        return (self._query(0, 0, self.n - 1, left, right, value))



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)