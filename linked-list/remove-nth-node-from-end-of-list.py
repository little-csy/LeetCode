# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return
        dummyHead = ListNode()
        dummyHead.next = head
        fast = dummyHead
        slow = dummyHead

        n += 1

        while n >0 :
            fast = fast.next
            n -= 1 

        while fast is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummyHead.next