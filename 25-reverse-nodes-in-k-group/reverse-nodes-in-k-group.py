# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, temp):
        previous = None
        while temp != None:
            front = temp.next
            temp.next = previous
            previous = temp
            temp = front
        return previous

    def kthNode(self, temp, k):
        k -= 1
        while temp != None and k > 0:
            k -= 1
            temp = temp.next
        return temp
    

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevLast = None
        while temp != None:
            Kth_Node = self.kthNode(temp, k)
            if Kth_Node == None:
                if prevLast:
                    prevLast.next = temp
                break
            nextNode = Kth_Node.next
            Kth_Node.next = None
            self.reverse(temp)
            if temp == head:
                head =Kth_Node
            else:
                prevLast.next = Kth_Node
            prevLast = temp
            temp = nextNode
        return head