# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque()
        q.append(root)
        val = 1
        while q:
            size = len(q)
            for _ in range(size):
                cur_node = q.popleft()
                if not cur_node.left and not cur_node.right:
                    return val
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            val += 1
        return val    