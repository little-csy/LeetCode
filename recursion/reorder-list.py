# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        last = slow.next
        slow.next = None
        prev = None
        
        while last:
            nxt = last.next
            last.next = prev
            prev = last
            last = nxt

        p1 = head
        p2 = prev

        while p1 and p2:
            nx1 = p1.next
            nx2 = p2.next
            p1.next = p2
            p2.next = nx1

            p1 = nx1
            p2 = nx2
        return head
        