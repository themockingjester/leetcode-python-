class Solution:
    
            
    def checkSubarraySum(self, nums, k):
        
        start=0
        previous=2
        end=previous
        if len(nums)<2:                     # if length of nums is smaller than 2
            return False
        if '0#0' in str('#'.join(map(str, nums))):          # if nums has at least 2 consequtive zeros
            return True
        p= sum(nums)
        
        
            
        if p%k==0:                      # if sum of nums is divisible by k
            
            return True
        elif p<k:                       # if sized of nums is smaller than k
            return False
        
        while True:
            
            temp = sum(nums[start:end])
            if temp%k==0:
                return True
             
            if len(nums[start:end])==len(nums):
                return False
            if end==len(nums):
                start=0
                previous+=1
                end=previous
                continue
            
            start+=1
            end+=1
