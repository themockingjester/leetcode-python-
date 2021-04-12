class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic = {}
        ctr=0
        for i in indices:
            dic[i]=s[ctr]
            ctr+=1
        k = ""
        
        for i in sorted(list(dic.keys())):
            
            k+=dic[i]
        return k
