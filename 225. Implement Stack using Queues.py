class MyStack:
    class Node():
        def __init__(self):
            self.val = None
            self.next = None
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.height = 0
        self.bottom = None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        k = MyStack.Node()
        k.val=x
        if self.height==0:
            self.bottom =k
            self.height+=1
        else:
            head = self.bottom
            while head:
                if head.next==None:
                    head.next=k
                    self.height+=1
                    break
                head = head.next


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        k = None
        if self.height==0:
            k=-1
        elif self.height==1:
            k = self.bottom.val
            self.bottom = None
            self.height-=1
        else:
            head = self.bottom
            while head:
                if head.next.next==None:
                    k = head.next.val
                    head.next=None
                    self.height-=1
                    break
                head = head.next
        return k
        
        
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.height==0:
            return -1
        head = self.bottom
        while head:
            if head.next==None:
                return head.val
            head = head.next

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.height==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
