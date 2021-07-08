class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        start=0
        end=10
        dic={}
        dic={}
        dic2={}
        if len(s)<10:
            return []
        while end<=len(s):
            temp = s[start:end]
            if temp not in dic:
                dic[temp]=1
            elif temp in dic:
                if len(dic2)==0:
                    dic2[1]={temp}
                else:
                    dic2[1].add(temp)
            start+=1
            end+=1
        if len(dic2)!=0:
            return dic2[1]
        return []
                
