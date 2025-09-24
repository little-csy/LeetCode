# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0 or lists is None:
            return 
        
        while len(lists)>1:
            tmp = []
            for i in range(0, len(lists),2):
                if i+1<len(lists):
                    tmp.append(self.merge2lists(lists[i], lists[i+1]))
                else:
                    tmp.append(lists[i])
            lists = tmp
        return lists[0]
                
        
    
    def merge2lists(self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val<=p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2
        return dummy.next