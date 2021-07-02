class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        
        start=0
        p=sorted(list(map(str, str(p))))
        s=list(map(str, str(s)))
        end=len(p)
        dic={}
        while end<len(s):
            if sorted(s[start:end])==p:
                dic[start]=1
            start+=1
            end+=1
        else:
            if sorted(s[start:end])==p:
                dic[start]=1
        return dic.keys()
        
