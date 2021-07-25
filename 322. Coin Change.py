
class Solution:
    def minCoins(self,coins,amount):
        if amount == 0:
            return 0
        ans = 9999999
        for i in coins:
            if amount-i>=0:
                if amount-i in self.dic:
                    subpblm=self.dic[amount-i]
                else:
                    subpblm = self.minCoins(coins,amount-i)
                    self.dic[amount-i]=subpblm
                if subpblm+1<ans:
                    ans=subpblm+1
        return ans
            
                    
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dic = {}
        
        self.lis = []
        out = self.minCoins(coins,amount)
        if out==9999999:
            return -1
        return out
        
        
        
        #                                                               Another approach by me
        
    class Solution:
        def coinChange(self, coins: List[int], amount: int) -> int:
            dp=[999999999]*(amount+1)
            dp[0]=0
            for i in coins:
                for j in range(1,amount+1):
                    if j-i<0:
                        continue
                    else:
                        dp[j]=min(dp[j],dp[j-i]+1)
            if dp[-1]==999999999:
                return -1
            else:
                return dp[-1]
        
        
        
        
        
        
        
        
        
