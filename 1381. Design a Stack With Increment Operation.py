class Node():
    def __init__(self):
        self.val = 0
        self.next = None
class CustomStack:
    
    def __init__(self, maxSize: int):
        self.height = 0  
        self.maxheight = maxSize
        self.bottom = None

    def push(self, x: int) -> None:
        k = Node()
        k.val = x
        if self.bottom==None:
            self.bottom = k
            self.height+=1
        else:
            head = self.bottom
            if self.height<self.maxheight:
                head = self.bottom
                while head:
                    if head.next == None:
                        head.next = k
                        self.height+=1
                        break
                    head = head.next
                

    def pop(self) -> int:
        if self.bottom == None:
            return -1
        elif self.height==1:
            k=self.bottom.val
            self.height-=1
            self.bottom = None
            return k
        else:
            head = self.bottom
            k = None
            while head:
                
                if head.next.next == None:
                    k = head.next.val
                    head.next = None
                    self.height -= 1
                    return k
                head = head.next
            
            

    def increment(self, k: int, val: int) -> None:
        head = self.bottom
        for i in range(k):
            if head == None:
                return
            else:
                head.val=head.val+val
                head = head.next


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
