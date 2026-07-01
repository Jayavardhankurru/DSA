# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while temp1 or temp2:
            summ = carry
            if temp1:
                summ +=  temp1.val
            if temp2:
                summ += temp2.val
            carry = summ // 10
            curr.next = ListNode(summ % 10)
            curr = curr.next
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
        return dummy.next