class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        ctr=0
        dic={}
        new1=""
        for i in s:
            
            if i not in dic:
                ctr+=1
                dic[i]=str(ctr)
                new1+=dic[i]
                
            else:
                new1+=dic[i]
        # print(new1)
        dic={}
        ctr=0
        new2=""
        for i in t:
            if i not in dic:
                ctr+=1
                dic[i]=str(ctr)
                new2+=dic[i]
                
            else:
                new2+=dic[i]
        # print(new2)
        if new1==new2:
            return True
        
        return False
            
