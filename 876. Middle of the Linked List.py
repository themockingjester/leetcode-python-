# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def middleNode(self, head: ListNode) -> ListNode:
        dic = {}
        ctr=0
        while head:
            ctr+=1
            dic[ctr]=head
            head = head.next
        
        length = len(dic)
        
        k = int(length/2)+1

            
        return dic[k]
        
            
