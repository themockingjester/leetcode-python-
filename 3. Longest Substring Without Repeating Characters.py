 # Approach sliding window           
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        maxlen=0
        setis=set()
        while i<len(s):
            ch = s[i]
            while ch in setis:
                setis.remove(s[j])
                j+=1
            setis.add(ch)
            maxlen = max(maxlen,i-j+1)
            i+=1
        return maxlen
            
                
            
'''
Correct Approach but slow and throws TLE
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ""
        start=0
        maxlen = 0
        for i in range(len(s)):
            if len(s[start:len(s)]) <= maxlen:
                continue
            new = ""
            for j in range(start,len(s)):
                new+=s[j]
                
                if len(list(map(str, str(new))))==len(set(list(map(str, str(new))))):
                    if len(new)>maxlen:
                        
                        maxlen=len(new)
                        
                else:
                    break
            start+=1
                         
                           
                           
                           
                           
                           
        return maxlen            
            
'''
