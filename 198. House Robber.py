class Solution:
    def solve(self,nums,curr,n):
        previous=0
        dp=nums.copy()
        for i in range(len(nums)):
            
            previous=i
            for j in range(i,len(nums)):
                
                if j==i:
                    
                    continue
                elif j>=previous+2:
                    t1=dp[previous]
                    t2=dp[j]
                    if t2>=t1+nums[j]:
                        continue
                    else:

                        dp[j]=t1+nums[j]
                        #previous=j

        return max(dp)
    def rob(self, nums: List[int]) -> int:
        
        
        
        return self.solve(nums,0,len(nums))
