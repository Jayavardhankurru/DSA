# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []
        parent_map = {}
        self.mapParent(root, parent_map)
        return self.bfsFromTarget(target, parent_map, k)
    def mapParent(self, root, parent_map):
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                parent_map[node.left] = node
                q.append(node.left)
            if node.right:
                parent_map[node.right] = node
                q.append(node.right)
    def bfsFromTarget(self, target, parent_map, k):
        q = deque()
        visited = set()
        q.append(target)
        visited.add(target)
        curr_level = 0
        while q:
            if curr_level == k:
                break
            for _ in range(len(q)):
                node = q.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    q.append(parent_map[node])
            curr_level += 1
        return [node.val for node in q]