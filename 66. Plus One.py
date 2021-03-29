class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=""
        for i in digits:
            k+=str(i)
        k=int(k)
        k+=1
        l = []
        while k!=0:
            l.append(k%10)
            k=k//10
        return l[::-1]
