# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverList(head):
            cur = head
            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = dummy
        while True:
            cnt = 0
            while cnt<k and end.next:
                end = end.next
                cnt += 1
            if cnt<k:
                return dummy.next
            
            nxtg = end.next
            end.next = None
            cur = start.next
            start.next = reverList(start.next)
            cur.next = nxtg
            start = cur
            end = cur
        return dummy.next
            
        