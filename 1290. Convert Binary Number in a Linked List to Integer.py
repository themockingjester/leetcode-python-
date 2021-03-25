# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def check(self,root):
        if root:
            self.s+=str(root.val)
            self.check(root.next)
    def getDecimalValue(self, head: ListNode) -> int:
        
        if head:
            self.s = ""
            self.check(head)
            print(self.s)
            return int(self.s,2)
