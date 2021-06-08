# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        lis = []
        
        while head:
            lis.append(head.val)
            head = head.next
        
        arr=[0]*len(lis)
        index=[0]
        for i in range(1,len(lis)):
            
            if lis[index[-1]]<lis[i]:
                j=-1
                while j>=-1*len(index) and lis[index[j]]<lis[i]:
                    ind = index.pop()
                    arr[ind]=lis[i]
                    
                index.append(i)
            else:
                index.append(i)
        return arr
                
                
