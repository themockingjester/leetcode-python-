class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[1]*(len(nums))
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if j<=i:
                    
                    continue
                else:
                    if nums[j]>nums[i]:
                        arr[j]=max(arr[i]+1,arr[j])
        return max(arr)
