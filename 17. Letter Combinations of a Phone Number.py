class Solution:
    def __init__(self):
        self.dic = {'0':" ",'1':".+@$", '2':"abc", '3':"def", '4':"ghi", '5':"jkl" , '6':"mno", '7':"pqrs" , '8':"tuv", '9':"wxyz"}
        self.res=[]
    def solve(self,n,ans,curr):
        if curr==len(n):
            self.res.append(ans)
            return
        for i in self.dic[n[curr]]:
            self.solve(n,ans+i,curr+1)
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        self.solve(digits,"",0)
        return self.res
