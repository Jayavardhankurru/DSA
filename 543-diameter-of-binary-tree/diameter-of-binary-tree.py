# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.findHeight(root)
        return self.diameter
    def findHeight(self, root):
        if not root:
            return 0
        lh = self.findHeight(root.left)
        rh = self.findHeight(root.right)
        self.diameter = max(self.diameter, lh + rh)
        return 1 + max(lh, rh)