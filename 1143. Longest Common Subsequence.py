class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        A=text1
        B=text2
        dp=[[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
        
        for j in range(1,len(B)+1):
            for i in range(1,len(A)+1):
                if B[j-1]==A[i-1]:
                    dp[j][i]=dp[j-1][i-1]+1
                else:
                    dp[j][i]=max(dp[j-1][i],dp[j][i-1])
        return dp[-1][-1]
                    
