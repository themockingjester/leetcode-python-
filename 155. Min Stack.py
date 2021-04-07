class MinStack:
    
    class ListNode():
        def __init__(self):
            self.next = None
            self.val = 0
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bottom = None
    
        self.height = 0
        

    def push(self, val: int) -> None:
        k = ListNode()
        k.val = val
        if self.bottom:
            head = self.bottom
            while head.next:
                head=head.next
            head.next = k
            self.height+=1
                
        else:
            self.bottom = k
            self.height+=1

    def pop(self) -> None:
        if self.bottom:
            head = self.bottom
            if self.height>2:
                while head:
                    if head.next.next==None:
                        head.next = None
                        self.height-=1
                        break
                    head=head.next
            elif self.height == 1:
                self.bottom = None
                self.height-=1
            else:
                self.bottom.next = None
                self.height-=1
                
            
                

    def top(self) -> int:
        if self.bottom:
            head = self.bottom
            if self.height>2:
                while head:
                    if head.next.next==None:
                        return head.next.val
                    head = head.next
            elif self.height==1:
                return head.val
            else:
                return head.next.val

    def getMin(self) -> int:
        minimum = None
        if self.bottom:
            head = self.bottom
            while head:
                if minimum == None:
                    minimum  = head.val
                elif head.val<minimum:
                    minimum = head.val
                    
                head = head.next
        return minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
