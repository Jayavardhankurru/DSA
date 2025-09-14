# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_nth_node(head, a):
        cnt = 1
        temp = head
        while temp != None:
            if cnt == a:
                return temp
            temp = temp.next
            cnt += 1
        return temp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        tail = head
        length = 1
        while tail.next != None:
            length += 1
            tail = tail.next
        if k % length == 0:
            return head
        k = k % length
        tail.next = head
        nth_node = Solution.find_nth_node(head, length-k)
        head = nth_node.next
        nth_node.next = None
        return head