# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lis=[]
        l=head
        while head:
            lis.append(head)
            head=head.next
        if len(lis)==1 and n==1:
            return None
        else:
            if n==len(lis) and n!=1:
                l=l.next
            elif n==1:
                lis[-1*(n+1)].next = None
            else:
                lis[-1*(n+1)].next = lis[-1*(n-1)]
        return l
