"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def  insertCopyNodes(self, head):
        temp = head
        while temp:
            copy = Node(temp.val)
            copy.next = temp.next
            temp.next = copy
            temp = temp.next.next
    
    def addRandomPointers(self, head):
        temp = head
        while temp:
            copy = temp.next
            if temp.random:
                copy.random = temp.random.next
            else:
                copy.random = None
            temp = temp.next.next
    
    def addNextPointers(self, head):
        temp = head
        dummy = Node(-1)
        res = dummy
        while temp:
            res.next = temp.next
            res = res.next
            temp.next = temp.next.next
            temp = temp.next
        return dummy.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        self.insertCopyNodes(head)
        self.addRandomPointers(head)
        return self.addNextPointers(head)