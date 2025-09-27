# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        start = dummy
        end = dummy
        while True:
            for i in range(k):
                end = end.next
                if end is None:
                    return dummy.next
            endnext = start.next
            startnext = end.next
            end.next = None
            start.next = self.reverlink(start.next)
            endnext.next = startnext
            start = endnext
            end = start
        
        return dummy.next

    def reverlink(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre