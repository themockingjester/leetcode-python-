class Solution:
    def maxPower(self, s: str) -> int:
        
        maxi = 0
        ctr=0
        for i in range(len(s)-1):
            
            if s[i]==s[i+1]:
                ctr+=1
                if ctr>maxi:
                    maxi=ctr
            else:
                ctr=0
        return maxi+1
            
        
                
