class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        ans = ""
        ctr=0
        for i in range(len(n)-1,-1,-1):
            
            
            if ctr==3:
                ans+="."
                ctr=0
                ans+=n[i]
                
            else:
                ans+=n[i]
            ctr+=1
        return ans[::-1]
