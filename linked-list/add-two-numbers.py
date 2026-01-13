# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        p1 = l1
        p2 = l2
        p = dummy
        flag = 0
        while p1 or p2:
            val = 0
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            node = ListNode(0, None)
            val += flag
            if val<10:
                node.val = val
                flag = 0
            else:
                node.val = val-10
                flag = 1
            p.next = node
            p = p.next
        
        if flag:
            node = ListNode(1, None)
            p.next = node

        return dummy.next