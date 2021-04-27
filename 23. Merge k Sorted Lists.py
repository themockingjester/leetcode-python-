# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lis=[]
        for i in lists:
            head = i
            while head:
                lis.append(head.val)
                head = head.next
        lis= sorted(lis)
        if len(lis)!=0:
            k = ListNode()
            k.val = lis[0]
            del lis[0]
            head = k
            out = head
            for i in lis:
                k = ListNode()
                k.val = i
                head.next = k
                head = head.next
            return out
            
