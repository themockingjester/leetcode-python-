class Solution:
    
    def check(self,s):
        print(s)
        for i in range(1,len(s)+1):
            self.ans+=i

                
    def countHomogenous(self, s: str) -> int:
        self.ans = 0
        k = set(list(map(str, str(s))))
        if len(k)==1:
            print(k)
            self.check(s)
            return self.ans%(10**9+7)
        if len(s)==1:
            return 1
        
        
        temp=""
        for i in range(len(s)-1):
            temp+=s[i]
            if s[i]==s[i+1]:
                pass
            else:
                self.check(temp)
                temp=""
            
                
        else:
            if(s[-1]==s[-2]):
                temp+=s[-1]
                self.check(temp)
            else:
                self.check(temp)
                self.ans+=1
        
        
        return self.ans%(10**9+7)
                
        
