# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


######################     With TWO Pointer Approach
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p=head
        q=head
        
        while True:
            if p == None:
                return False
            elif (p.next!=None and p.next.next!=None):
                p=p.next.next
            else:
                return False
            if q==None:
                return False   
            elif q.next!=None:
                q=q.next
            else:
                return False
            if p==q:
                return True
