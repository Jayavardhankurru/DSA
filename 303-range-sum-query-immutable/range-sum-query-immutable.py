class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, nums)

    def build(self, node, left, right, nums):
        if left == right:
            self.tree[node] = nums[left]
            return
        mid = (left + right) // 2
        self.build(2 * node + 1, left, mid, nums)
        self.build(2 * node + 2, mid + 1, right, nums)
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
# param_1 = obj.sumRange(left,right)