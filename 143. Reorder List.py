# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        if len(lis)%2==0:
            n = len(lis)//2
            lis1 = lis[0:n]
            lis2 = lis[n:]
            lis2 = lis2[::-1]
            lis3 = []
            
            for i in range(len(lis1)):
                
                lis3.extend((lis1[i],lis2[i]))
                
            out = node
            ctr = 0
            while node:
                node.val = lis3[ctr]
                
                ctr+=1
                node = node.next
            return out
        else:
            n = len(lis)//2
            lis1=lis[0:n]
            lis2=lis[n+1:]
            lis2 = lis2[::-1]
            lis3 = []
            
            for i in range(len(lis1)):
                
                lis3.extend((lis1[i],lis2[i]))
            lis3.append(lis[n])
            out = node
            ctr = 0
            while node:
                node.val = lis3[ctr]
                
                ctr+=1
                node = node.next
            return out
