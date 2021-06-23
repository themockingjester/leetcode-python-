class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        ans = ""
        start=0
        maxlen = 0
        for i in range(len(s)):
            if len(s[start:len(s)]) <= maxlen:
                continue
            new = ""
            for j in range(start,len(s)):
                
                new+=s[j]
                if new==new[::-1]:
                    if len(new)>maxlen:
                        maxlen=len(new)
                        ans = new
                
            start+=1
                         
                           
                           
                           
                           
                           
        return ans
                          
            
