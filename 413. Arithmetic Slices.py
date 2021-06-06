class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        N = 0
        for i in range(len(nums)-2):
            
            while i+2<len(nums) and nums[i]+nums[i+2] == 2*nums[i+1]:
                
                
                N += 1
                i += 1
            
            
        return N
