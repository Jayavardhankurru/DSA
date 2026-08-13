class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, nums)
        
    def build(self, node, start, end, nums):
        if start == end:
            self.tree[node] = nums[start]
            return
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid, nums)
        self.build(2 * node + 2, mid + 1, end, nums)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index: int, val: int) -> None:
        self.updateTree(0, 0, self.n - 1, index, val)
    
    def updateTree(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
            return 
        mid = (start + end) // 2
        if index <= mid:
            self.updateTree(2 * node + 1, start, mid, index, val)
        else:
            self.updateTree(2 * node + 2, mid + 1, end, index, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def sumRange(self, left: int, right: int) -> int:
        return self.query(0, 0, self.n - 1, left, right)
    
    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        leftSum = self.query(2 * node + 1, start, mid, left, right)
        rightSum = self.query(2 * node + 2, mid + 1, end, left, right)
        return leftSum + rightSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)