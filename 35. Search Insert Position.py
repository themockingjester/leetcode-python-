class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target<min(nums):
            return 0
        if target>max(nums):
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i+1]>target:
                return i+1
        
                
            
