class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k = len(nums)
        nums = list(set(nums))
        dic={}
        lis=[]
        
        for i in nums:
            dic[i]=1
        ctr=1
        while ctr<=k:
            
            if ctr not in dic:
                lis.append(ctr)
            ctr+=1
        
        return lis
