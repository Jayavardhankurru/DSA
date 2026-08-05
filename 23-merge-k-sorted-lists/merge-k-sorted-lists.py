# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for head in lists:
            while head:
                arr.append(head.val)
                head = head.next
        arr.sort()
        dummy = ListNode(-1)
        curr = dummy
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
