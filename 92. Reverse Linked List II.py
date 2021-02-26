class Solution:
    def add(self,val,node):
        k = ListNode()
        k.val = val
        curr = node
        while curr.next != None:
            curr= curr.next
        curr.next = k
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        curr = head
        ctr = 1
        if left == right:
            return head
        try:
            flag = False
            while curr.next!=None:
                if ctr == left:
                    starting = curr
                elif ctr==right:
                    ending = curr
                    flag = True
                ctr+=1
                curr = curr.next
            if flag == False:
                ending = curr
            curr = starting
            lis = []
            while curr!=ending:
                lis.append(curr.val)
                curr = curr.next
            lis.append(curr.val)
            lis.reverse()
            dummy = ListNode()
            for i in lis:
                self.add(i,dummy)
            #return dummy.next
            if left==1:
                head = dummy.next
            else:
                curr = head
                while curr.next != starting:
                    curr = curr.next
                curr.next = dummy.next
            
            curr = head
            while curr.next != None:
                curr = curr.next
            curr.next = ending.next
             
        except:
            pass
        return head

            
