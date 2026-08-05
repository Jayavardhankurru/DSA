# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        stack = []
        for i in arr:
            while stack and stack[-1] < i:
                stack.pop()
            stack.append(i)
        dummy = ListNode(-1)
        curr = dummy
        for num in stack:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next