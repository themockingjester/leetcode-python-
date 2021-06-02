class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ctr=0
        lis=[]
        ctr2=1
        while ctr<k:
            
            if ctr2 not in arr:
                lis.append(ctr2)
                ctr+=1
            ctr2+=1
            
        return lis[-1]
