# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lis = []
        head = l1
        while head:
            lis.append(head.val)
            head = head.next
        head = l2
        while head:
            lis.append(head.val)
            head = head.next
        lis = sorted(lis)
        k= ListNode()
        out = k
        if len(lis)==0:
            return None
        k.val = lis[0]
        del lis[0]
        for i in lis:
            p= ListNode()
            p.val = i
            k.next = p
            k = k.next
        return out
