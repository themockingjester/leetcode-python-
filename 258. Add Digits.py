class Solution:
    def addDigits(self, num: int) -> int:
        z = str(num)
        while(len(z)!=1):
            sum = 0
            for i in z:
                sum+=int(i)
            z=str(sum)
        else:
            return int(z)
        
