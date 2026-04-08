# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        pre = None
        p = head2
        while p:
            nxt = p.next
            p.next = pre
            pre = p
            p = nxt
        newhead = pre

        p1 = head
        p2 = newhead

        while p2:
            p1nxt = p1.next
            p2nxt = p2.next
            p1.next = p2
            p1 = p1nxt
            p2.next = p1
            p2 = p2nxt
        return head

        