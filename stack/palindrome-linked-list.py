# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        cur = slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur =nxt
        
        p2 = pre
        p1 = head
        while p1 and p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        
        if p1 or p2:
            return False
        return True

        