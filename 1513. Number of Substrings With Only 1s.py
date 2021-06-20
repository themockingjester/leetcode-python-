class Solution:
    def numSub(self, s: str) -> int:
        curr=0
        ans=0
        for i in range(len(s)):
            if s[i]=='1':
                curr+=1
            else:
                if curr!=0:
                    ans+=sum(range(1,curr+1))
                    curr=0
        else:
            if curr!=0:
                ans+=sum(range(1,curr+1))
        return ans%(1000000000+7)
                    
