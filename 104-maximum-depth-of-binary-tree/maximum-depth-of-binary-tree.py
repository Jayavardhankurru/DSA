from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = Queue()
        level = 0
        q.put(root)
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                front = q.get()
                if front.left:
                    q.put(front.left)
                if front.right:
                    q.put(front.right)
            level += 1
        return level
