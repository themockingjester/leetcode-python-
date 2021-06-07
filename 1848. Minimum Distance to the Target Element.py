class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        lis = []
        if nums.count(target)>1:
            for i in range(len(nums)):
                if nums[i]==target:
                    
                    lis.append(abs(i-start))
            print(lis)
            return min(lis)
        return abs(nums.index(target,0,len(nums))-start)
