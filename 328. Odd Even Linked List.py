# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ctr=1
        even=[]
        odd=[]
        while head:
            if ctr%2==0:
                even.append(head.val)
            else:
                odd.append(head.val)
            ctr+=1
            head = head.next
        head = ListNode(1)
        j = head
        for i in odd:
            k = ListNode(i)
            j.next = k
            j  = k
        for i in even:
            k = ListNode(i)
            j.next = k
            j  = k
        return head.next
