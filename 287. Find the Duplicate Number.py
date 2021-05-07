class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        dic={}
        while start<end:
            if nums[start] in dic:
                return nums[start]
            else:
                dic[nums[start]]=1
            if nums[end] in dic:
                return nums[end]
            else:
                dic[nums[end]]=1
            start+=1
            end-=1
        if len(nums)%2!=0:
            mid = nums[len(nums)//2]
            if mid in dic:
                return mid
            
            
