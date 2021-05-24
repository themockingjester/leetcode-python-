class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t=sorted(t)
        print(s,t)
        ctr=0
        for i in range(len(t)):
            if t[i] in s:
                s.remove(t[i])
            else:
                return t[i]
            
        
