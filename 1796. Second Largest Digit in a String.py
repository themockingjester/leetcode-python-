class Solution:
    def secondHighest(self, s: str) -> int:
        lis=[]
        for i in s:
            if i in '0123456789':
                lis.append(int(i))
                
        if len(lis)==0:
            return -1
        
        
        lis = list(set(lis))
        lis= sorted(lis)
        lis = lis[::-1]
        print(lis)
        if len(lis)==1:
            return -1
        
        return lis[1]
