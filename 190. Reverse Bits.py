class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n).replace("0b", "")
        
        n=n[::-1]
        while(len(n)<=31):
            n+='0'
        n="0b"+n
        return int(n,2)
        
