class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start=0
        end=len(nums)
        while start<=end:
            
            if start==end:
                if start not in nums:
                    return start
            
            if start not in nums:
               
                return start
            if end not in nums:
                return end
            
            start+=1
            end-=1
        return start
