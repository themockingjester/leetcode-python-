# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def check(self,root):
        if root:
            self.lis.append(root)
            self.check(root.next)
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        self.lis = []
        if head:
            self.check(head)
            temp = self.lis[k-1].val
            self.lis[k-1].val = self.lis[-1*k].val
            self.lis[-1*k].val = temp
        return head
