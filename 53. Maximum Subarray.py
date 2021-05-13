class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lis = [0 for i in range(len(nums))]
        lis[0]=nums[0]
        for i in range(1,len(nums)):
            lis[i]=max(lis[i-1]+nums[i],nums[i])
        print(lis)
        return max(lis)
