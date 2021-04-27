# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        ctr = 0
        lis2 = []
        lis3 = []
        for i in lis:
            if ctr<k:
                lis2.append(i)
            else:
                lis3.extend(lis2[::-1])
                ctr = 0
                lis2 = []
                lis2.append(i)
            ctr+=1
        else:
            if len(lis2)==k:
                lis2 = lis2[::-1]
        lis3.extend(lis2)
        if len(lis3)==0:
            return None
        k = ListNode()
        out = k
        k.val = lis3[0]
        del lis3[0]
        for i in lis3:
            p = ListNode()
            p.val = i
            k.next = p
            k = k.next
        return out
            
            
                
