# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode()
        cur = dummy
        carry = 0
        while p1 or p2 or carry:
            if p1:
                val1 = p1.val
            else:
                val1 = 0
            if p2:
                val2 = p2.val
            else:
                val2 = 0
            total = val1+val2+carry
            carry = total//10
            new = ListNode(total%10)
            cur.next = new
            cur = new
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        return dummy.next
        
        