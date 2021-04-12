# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lis=[]
        head2 = head
        while head2:
            lis.append(head2.val)
            head2 = head2.next
        lis = sorted(lis)
        head2= head
        ctr=0
        while head2:
            head2.val = lis[ctr]
            ctr+=1
            head2 = head2.next
        return head
