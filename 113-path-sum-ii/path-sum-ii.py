# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        if not root:
            return self.ans
        self.dfs(root, targetSum, 0, [])
        return self.ans
     
    def dfs(self, root, targetSum, summ, temp):
        summ += root.val
        temp.append(root.val)
        if not root.left and not root.right and summ == targetSum:
            self.ans.append(temp[:])
        if root.left:
            self.dfs(root.left, targetSum, summ, temp)
        if root.right:
            self.dfs(root.right, targetSum, summ, temp)
        temp.pop()