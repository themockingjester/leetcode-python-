# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


############################      With Two pointer
class Solution:
    def detectLoop(self,head):
        self.slow=head
        self.fast=head
        while True:
            if self.slow==None:
                return False
            elif self.slow.next==None:
                return False
            else:
                self.slow = self.slow.next
            if self.fast==None:
                return False
            elif self.fast.next!=None and self.fast.next.next!=None:
                self.fast=self.fast.next.next
            else:
                return False
            if self.fast==self.slow:
                return True
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hasLoop = self.detectLoop(head)
        if(hasLoop):
            ind=0
            start=head
            slow2=self.slow
            while start!=slow2:
                
                start=start.next
                slow2=slow2.next
                ind+=1
            return start
        return None
