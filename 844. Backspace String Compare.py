class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lis = []
        
        for i in s:
            if i=="#":
                if len(lis)!=0:
                    lis.pop(-1)
            else:
                lis.append(i)
        lis2=[]
        for i in t:
            if i=="#":
                if len(lis2)!=0:
                    lis2.pop(-1)
            else:
                lis2.append(i)
        print(lis,lis2)
        if lis==lis2:
            return True
        else:
            return False
            
