# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        q = deque([root])
        while q:
            size = len(q)
            flagx = False
            flagy = False
            for i in range(size):
                node = q.popleft()
                if node.val == x:
                    flagx = True
                if node.val == y:
                    flagy = True
                if node.left and node.right:
                    if ((node.left.val == x and node.right.val == y) or 
                        (node.left.val == y and node.right.val == x)):
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flagx and flagy:
                return True
            if flagx or flagy:
                return False
        return False