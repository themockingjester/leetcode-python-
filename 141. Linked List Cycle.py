# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if  head==None or head.next==None or head.next.next==None:
            return False
        curr=head
        dito={}
        while curr:
            curr=curr.next

            if curr in dito:
                return True
            else:
                dito[curr]=1
        return False
            
        
