# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        q =  deque()
        q.append(root)
        result = ""
        while q:
            node = q.popleft()
            if node is None:
                result  += "#,"
            else:
                result += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque()
        q.append(root)
        i = 1
        while q and i < len(nodes) - 1:
            cur_node = q.popleft()
            if nodes[i] != "#":
                left = TreeNode(int(nodes[i]))
                cur_node.left = left
                q.append(left)
            i += 1
            if nodes[i] != "#":
                right = TreeNode(int(nodes[i]))
                cur_node.right = right
                q.append(right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))