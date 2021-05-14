class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        
        b= int(b,2)
        sumis = a+b
        c=str(bin(sumis))
        return c[2:]
