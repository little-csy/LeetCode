# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        arr = []
        while p:
            arr.append(p.val)
            p = p.next
        
        arr.sort()

        dummy = ListNode(0)
        p = dummy
        for v in arr:
            q = ListNode(v)
            p.next = q
            p = p.next
        
        return dummy.next