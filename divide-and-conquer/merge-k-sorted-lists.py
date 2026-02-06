# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)

        def mergeL(l1, l2):
            dummy = ListNode(0)
            p = dummy
            p1 = l1
            p2 = l2

            while p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            
            if p1:
                p.next = p1
            if p2:
                p.next = p2
            
            return dummy.next

        interval = 1
        while interval<n:
            for i in range(0, n-interval, 2*interval):
                lists[i] = mergeL(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]

        
    
    