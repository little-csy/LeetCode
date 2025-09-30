# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        p1 = headA
        c1 = 0
        p2 = headB
        c2 = 0
        while p1:
            p1 = p1.next
            c1 += 1
        while p2:
            p2 = p2.next
            c2 += 1
        
        if c1 > c2:
            d = c1 - c2
            p1 = headA
            p2 = headB
            while d:
                p1 = p1.next
                d -= 1
            while p1 and p2:
                if p1 == p2:
                    return p1
                p1 = p1.next
                p2 = p2.next
            return None
        
        else:
            d = c2 - c1
            p1 = headA
            p2 = headB
            while d:
                p2 = p2.next
                d -= 1
            while p1 and p2:
                if p1 == p2:
                    return p1
                p1 = p1.next
                p2 = p2.next
            return None


        