class Solution:
    def solve(self,curr,s,n,ans):
        
        if curr==n:
            self.res.insert(0,ans)
            return
        
        if s[curr].isalpha():
            if s[curr].isupper():
                self.solve(curr+1,s,n,ans[:]+s[curr].lower())
            else:
                self.solve(curr+1,s,n,ans[:]+s[curr].upper())
            self.solve(curr+1,s,n,ans[:]+s[curr])
        else:
            self.solve(curr+1,s,n,ans[:]+s[curr])
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res=[]
        self.solve(0,s,len(s),"")
        return self.res
