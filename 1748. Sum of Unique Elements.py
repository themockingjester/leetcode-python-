class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        sumwillbe=0
        while start<=end:
            if start==end and nums.count(nums[start])==1:
                sumwillbe+=nums[start]
            else:
                if nums.count(nums[start])==1:
                    sumwillbe+=nums[start]
                if nums.count(nums[end])==1:
                    sumwillbe+=nums[end]
            start+=1
            end-=1
        
        return sumwillbe
