class Solution:
    def sumBase(self, n: int, k: int) -> int:
        num=""
        while(n!=0):
            num+=str(n%k)
            
            n=n//k
        
        num=num[::-1]
        ctr=0
        for i in num:
            ctr+=int(i)
        return ctr
