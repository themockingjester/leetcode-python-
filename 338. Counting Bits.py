class Solution:
    def countBits(self, num: int) -> List[int]:
        lis=[]
        for i in range(num+1):
            n = bin(i).replace("0b","")
        
            n = [int(k) for k in n]
            lis.append(sum(n))
        return lis
