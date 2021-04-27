# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lis = []
        
        while head:
            lis.append(head.val)
            head = head.next
        if len(lis)==0:
            return
        lis2 = []   
        for i in range(len(lis)):
            if lis[i]<x:
                lis2.append(lis[i])
                lis[i] = " "
        
        for i in lis:
            if i==" ":
                pass
            else:
                lis2.append(i)
        k = ListNode()
        head = k
        k.val = lis2[0]
        del lis2[0]
        for i in lis2:
            p = ListNode()
            p.val = i
            k.next = p
            k = k.next
        return head
        
          
