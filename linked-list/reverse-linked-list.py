# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        pre = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            
        return pre