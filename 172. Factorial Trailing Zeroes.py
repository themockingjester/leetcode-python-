class Solution:
    def trailingZeroes(self, n: int) -> int:
        product=1
        while(n>=1):
            product*=n
            n-=1
        s = str(product)
        print(s)
        s=s[::-1]
        ctr=0
        for i in s:
            if i!='0':
                break
                
            else:
                ctr+=1
        return ctr
