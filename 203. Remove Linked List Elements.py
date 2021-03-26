# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def check(self,root,val):
        if root:
            if root.next:
                
                if root.next.val==val:
                    
                    root.next = root.next.next
                    self.check(root,val)
                else:
                    self.check(root.next,val)
            
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        self.main = head
        if head:
            while head.next and head.val == val:
                
                self.main = head.next
                head = head.next
            if head.next==None and head.val == val:
                return None
            if head.next:
                
                if head.next.val==val:
                    head.next = head.next.next
                    self.check(head,val)
                else:
                    self.check(head.next,val)
                    
        return self.main
