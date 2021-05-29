class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        ctr=0
        last = 0
        for i in customers:
            last = max(i[0],last)
            last=last+i[1]-i[0]
            
            total+=abs(last)
            last+=abs(i[0])
            ctr+=1
        return total/ctr
            
            
