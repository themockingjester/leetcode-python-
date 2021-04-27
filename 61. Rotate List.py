# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        lis = []
        root = head
        while root:
            lis.append(root.val)
            root = root.next
        k = k%len(lis)
        lis[:]=lis[-k:]+lis[0:-k]
        root = head
        while root:
            root.val = lis[0]
            del lis[0]
            root = root.next
        return head
