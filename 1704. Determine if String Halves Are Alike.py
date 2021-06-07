class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        ctr1=0
        ctr2=0
        lis =['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
        for i in s[0:len(s)//2]:
            if i in lis:
                ctr1+=1
        for i in s[len(s)//2:]:
            if i in lis:
                ctr2+=1
        if ctr1==ctr2:
            return True
        else:
            return False
