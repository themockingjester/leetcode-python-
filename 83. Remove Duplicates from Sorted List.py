# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        lis=[]
        while head:
            lis.append(head.val)
            head = head.next
        new = []
        for i in lis:
            if i not in new:
                new.append(i)
        lis = new
        if len(lis)==0:
            return
        k=ListNode()
        k.val = lis[0]
        out = k
        del lis[0]
        
        for i in lis:
            p=ListNode()
            p.val = i
            k.next = p
            k = k.next
        return out
        
