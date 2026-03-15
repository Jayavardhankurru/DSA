# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        max_width = 0
        q = deque()
        q.append((root, 0))
        while q:
            size = len(q)
            min_idx = q[0][1]
            first, last = 0, 0
            for i in range(size):
                node, idx = q.popleft()
                curr_idx = idx - min_idx
                if i == 0:
                    first = curr_idx
                if i == size - 1:
                    last = curr_idx
                if node.left:
                    q.append((node.left, 2 * curr_idx + 1))
                if node.right:
                    q.append((node.right, 2 * curr_idx + 2))
            max_width = max(max_width, last - first + 1)
        return max_width