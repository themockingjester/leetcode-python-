class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s=""
        for i in range(1,n+1):
            s+=str(bin(i))[2:]
        
        return int("0b"+s,2)%(1000000000+7)
