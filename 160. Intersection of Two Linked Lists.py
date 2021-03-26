# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def check(self,root):
        if root:
            if root not in self.dic:
                self.dic[root] = True
                self.check(root.next)
            else:
                self.var = root
                
                return
        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        self.dic = {}
        self.var = None
        if headA:
            self.check(headA)
        if headB:
            if headB in self.dic:
                return headB
            else:
                self.check(headB)
        return self.var
            
