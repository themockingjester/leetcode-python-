"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.lis=[]
        k=head
        while head:
            
            if head.child:
                if head.next:
                    self.lis.append(head.next)
                head.next = head.child
                head.child.prev = head
                head.child = None
                
            if head.next==None:
                if len(self.lis)!=0:
                    head.next = self.lis[-1]
                    self.lis[-1].prev = head
                    del self.lis[-1]
            head = head.next
        return k
        
