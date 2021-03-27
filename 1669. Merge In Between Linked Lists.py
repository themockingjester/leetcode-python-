# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ctr = 0
        self.begin = list1
        lis= []
        if a==0:
            self.begin = list2
            while list1:
                
                if ctr == b+1:
                    lis.append(list1)
                    break
                ctr+=1
                list1 = list1.next
        else:
            while list1:
                if ctr == a-1:
                    lis.append(list1)
                if ctr == b+1:
                    lis.append(list1)
                    break
                ctr+=1
                list1 = list1.next
        
        if len(lis)==1:
            head = self.begin
            while head:
                if head.next:
                    head = head.next
                else:
                    head.next = lis[0]
                    break
            return self.begin
        else:
            lis[0].next = list2
            head = list2
            while head:
                if head.next:
                    head = head.next
                else:
                    head.next = lis[1]
                    break
            
            return self.begin
            
                        
                
                
            
            
            
