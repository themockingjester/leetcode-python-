# Using two pointer approach

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        start = 0
        ans = 0
        end = len(height)-1
        leftmax = start
        rightmax = end
        
        while start < end:
            if height[start] < height[end]:
                if height[start]>=height[leftmax]:
                    leftmax = start
                else:
                    ans += height[leftmax]-height[start]
                start+=1
            else:
                if height[end]>=height[rightmax]:
                    rightmax = end
                else:
                    ans += height[rightmax]-height[end]
                end-=1
        return ans
# Using prefix Sum

class Solution:
    def trap(self, height: List[int]) -> int:
        prefixArr = []
        prefixMax=0
        for i in height:
            if i>prefixMax:
                prefixMax=i
            prefixArr.append(prefixMax)
        suffixArr = []
        suffixMax=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>suffixMax:
                suffixMax=height[i]
            suffixArr.append(suffixMax)
        suffixArr=suffixArr[::-1]
        totalWater=0
        for i in range(len(height)):
            totalWater+=min(prefixArr[i],suffixArr[i])- height[i]
        return totalWater

        
                

                
            
