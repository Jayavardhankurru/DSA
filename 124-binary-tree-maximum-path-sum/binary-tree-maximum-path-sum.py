# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        self.pathSum(root, self.maxi)
        return self.maxi
    
    def pathSum(self, root, maxi):
        if not root:
            return 0
        lh = max(0, self.pathSum(root.left , maxi))
        rh = max(0, self.pathSum(root.right , maxi))
        self.maxi = max(self.maxi, lh + rh + root.val)
        return root.val + max(lh, rh)