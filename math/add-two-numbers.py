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
            total = carry
            if p1:
                total += p1.val
                p1 = p1.next

            if p2:
                total += p2.val
                p2 = p2.next

            carry = total//10
            new = ListNode(total%10)
            cur.next = new
            cur = new

        return dummy.next