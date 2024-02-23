# First solution

class MyQueue:

    def __init__(self):
        self.inputQueue = []
        self.outputQueue=[]

    def push(self, x: int) -> None:
        self.inputQueue.append(x)

    def pop(self) -> int:
        if len(self.outputQueue)>0:
            return self.outputQueue.pop()
        else:
            while len(self.inputQueue)>0:
                self.outputQueue.append(self.inputQueue.pop())
            return self.outputQueue.pop()

    def peek(self) -> int:
        if len(self.outputQueue)>0:
            return self.outputQueue[-1]
        else:
            while len(self.inputQueue)>0:
                self.outputQueue.append(self.inputQueue.pop())
            return self.outputQueue[-1]

    def empty(self) -> bool:
        return len(self.inputQueue)==0 and len(self.outputQueue)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# Another solution
class MyQueue:
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
        Push element x to the back of queue.
        """
        k = MyQueue.Node()
        k.val = x
        
        if self.height == 0:
            self.bottom = k
            self.height+=1
        else:
            
            k.next = self.bottom
            self.bottom = k
            self.height+=1
        
            
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        k = None
        if self.height == 1:
            k = self.bottom.val
            self.bottom = None
            self.height-=1
        elif self.height == 0:
            k = -1
        
        else:
            
            head = self.bottom
            while head:
                if head.next.next == None:
                    k = head.next.val
                    head.next = None
                    self.height-=1
                    break
                head = head.next
        return k
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.height==0:
            return -1
        else:
            head = self.bottom
            while head:
                if head.next==None:
                    return head.val
                head = head.next
            
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.height == 0:
            return True
        else:
            return False        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
