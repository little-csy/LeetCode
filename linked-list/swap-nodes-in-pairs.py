# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        cur = dummyHead

        while cur.next is not None and cur.next.next is not None:
            temp1 = cur.next
            temp2 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = temp1
            temp1.next = temp2
            cur = temp1

        return dummyHead.next