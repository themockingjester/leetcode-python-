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
                

                
            
