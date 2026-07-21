# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        i = 1
        while curr and i < n // 2:
            curr = curr.next
            i += 1
        curr2 = curr.next
        prev = None
        while curr2:
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        curr = head
        curr1 = prev
        maxi = 0
        while curr and curr1:
            maxi = max(maxi, curr.val + curr1.val)
            curr = curr.next
            curr1 = curr1.next
        return maxi
        
