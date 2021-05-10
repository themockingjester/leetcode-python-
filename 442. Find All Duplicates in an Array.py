class Solution:
    
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lis = {}
        start=0
        lis2=[]
        end=len(nums)-1
        while start<=end:
            if start==end:
                if nums[start] in lis:
                    lis2.append(nums[start])
            else:
            
                if nums[start] in lis:
                    lis2.append(nums[start])
                else:
                    lis[nums[start]]=1
                if nums[end] in lis:
                    lis2.append(nums[end])
                else:
                    lis[nums[end]]=1
            start+=1
            end-=1
        return lis2
