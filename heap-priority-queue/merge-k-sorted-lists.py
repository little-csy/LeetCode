# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if not lists:
            return None

        def merge2list(l1, l2):
            dummy = ListNode()
            p = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return dummy.next
        
        interval = 1
        while interval < n:
            for i in range(0, n-interval, 2*interval):
                lists[i] = merge2list(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]