# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic = {}
        while head:
            if head not in dic:
                dic[head]=1
            else:
                return head
            head = head.next
            
