class Solution:
    def isGood(self,s):
        lis=list(map(str, str(s)))
        setis = list(set(lis))
        if len(setis)==len(lis):
            return True
        else:
            return False
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        ctr=0
        for i in range(len(s)-2):
            print(s[i:i+3])
            if self.isGood(s[i:i+3]):
                ctr+=1
        return ctr
