# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None

        pre = None
        p = l2

        while p:
            nxt = p.next
            p.next = pre
            pre = p
            p = nxt
        
        p1 = head
        p2 = pre
        
        while p1 and p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        
        return True