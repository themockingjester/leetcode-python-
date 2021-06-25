class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        if len(set(nums))==1 and 1 in nums and k!=1:
            k=len(nums)
            s=0
            for i in range(1,k+1):
                s+=i
            return s
            
        ctr=0
        for i in range(len(nums)):
            if nums[i]<k:
                ctr+=1
            var=[nums[i]]
            start=i+1
            for j in range(start,len(nums)):
                var = var.copy()
                var[0] = var[0]*nums[j]
                if var[0]<k:
                    
                    ctr+=1
                else:
                    break
        return ctr
