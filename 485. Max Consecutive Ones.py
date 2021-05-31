class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ctr=0
        maxi = 0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]==1:
                ctr+=1
                if ctr>maxi:
                    maxi=ctr
            else:
                ctr=0
        if 1 not in nums:
            return 0
        return maxi+1
