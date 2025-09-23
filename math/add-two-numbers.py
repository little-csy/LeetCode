# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        head = ListNode()
        p3 = head
        flag = 0
        while p1 or p2:
            if p1 is None and p2:
                if flag == 0:
                    val = p2.val
                    flag = 0
                else:
                    if p2.val+1>=10:
                        val = p2.val-9
                        flag = 1
                    else:
                        val = p2.val+1
                        flag = 0
                p2 = p2.next
            if p2 is None and p1:
                if flag == 0:
                    val = p1.val
                    flag = 0
                else:
                    if p1.val+1>=10:
                        val = p1.val-9
                        flag = 1
                    else:
                        val = p1.val+1
                        flag = 0
                p1 = p1.next
            if p1 and p2:
                if p1.val+p2.val >= 10:
                    if flag == 0:
                        val = p1.val+p2.val-10
                        flag = 1
                    else:
                        val = p1.val+p2.val-9
                        flag = 1
                else:
                    if flag == 0:
                        val = p1.val+p2.val
                        flag = 0
                    else:
                        val = p1.val+p2.val+1
                        if val >= 10:
                            flag = 1
                        else:
                            flag = 0
                p1 = p1.next
                p2 = p2.next
            new = ListNode(val, None)
            p3.next = new
            p3 = new
        if flag == 1:
            new = ListNode(1, None)
            p3.next = new
        return head.next
        