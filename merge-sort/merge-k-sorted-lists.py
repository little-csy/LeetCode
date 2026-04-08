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
        interval = 1
        
        def mergetwo(l1,l2):
            dummy = ListNode(0)
            p = dummy
            while l1 and l2:
                if l1.val<=l2.val:
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
        while interval<n:
            for i in range(0,n-interval,2*interval):
                lists[i] = mergetwo(lists[i],lists[i+interval])
            interval *=2
        return lists[0]