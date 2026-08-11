# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum = []
        q = deque([root])
        while q:
            size = len(q)
            currSum = 0
            for i in range(size):
                node = q.popleft()
                currSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelSum.append(currSum)
        maxi = float("-inf")
        level = 0
        for ind, num in enumerate(levelSum):
            if num > maxi:
                maxi = num
                level = ind
        return level + 1
