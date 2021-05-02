# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        k = head
        lis = []
        while k:
            lis.append(k.val)
            k = k.next
        for i in range(1,len(lis)):
            for j in range(i):
                if lis[i]<lis[j]:
                    temp = lis[j]
                    lis[j]=lis[i]
                    lis[i]= temp
        print(lis)
        head2 = head
        while head2:
            head2.val = lis[0]
            del lis[0]
            head2 =head2.next
        return head
