# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        
        while cur.next is not None and cur.next.next is not None:
            p1 = cur.next
            p2 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = p1
            p1.next = p2
            cur = p1
        return dummy.next