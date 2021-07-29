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
       
#                                                               Another approach by me 
#                                                       time complexity-O(N^2)            Space Complexity-O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        val = nums
        n=len(nums)
        dp=[1]*(n)
        for i in range(n):

            for j in range(n):
                if j<=i:
                    continue
                else:
                    if val[j]>val[i]:
                        dp[j]=max(dp[j],dp[i]+1)

        return(max(dp))
