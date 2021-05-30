class Solution:
    def arrangeCoins(self, n: int) -> int:
        ctr=0
        ctr2=1
        while(n-ctr2>=0):
            n-=ctr2
            ctr+=1
            ctr2+=1
        return ctr
    
            
            
