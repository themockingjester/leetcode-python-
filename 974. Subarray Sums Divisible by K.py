class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic={}
        dic[0]=1
        sums=0
        count=0
        for i in nums:
            sums+=i
            
            count+=dic.get(sums%k,0)
            dic[sums%k]=dic.get(sums%k,0)+1
        return count       
                
                
                
