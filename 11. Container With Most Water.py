# my approach but with recursion hence throughing TLE at test case 55 out of 60
# class Solution:
#     def check(self,lower,upper):
#         if lower < upper:
#             base = len(self.lis[lower:upper])
#             print(base)
#             if self.lis[lower]>=self.lis[upper]:
#                 height = self.lis[upper]

#                 area = height*base
#                 if area>self.max:
#                     self.max = area
#                     print("height"+str(height))
#                     print("base"+str(base))
#                 self.check(lower,upper-1)
#             else:
#                 height = self.lis[lower]

#                 area = height*base
#                 if area>self.max:
#                     self.max = area
#                     print("height"+str(height))
#                     print("base"+str(base))
#                 self.check(lower+1,upper)
        
        
#     def maxArea(self, height: List[int]) -> int:
#         self.lis = height
#         self.max = 0
#         self.check(0,len(self.lis)-1)
#         return self.max
    
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        maxarea = 0
        end =  len(height)-1
        while(start < end):
            s = min(height[start],height[end]) * (end - start)

            if s > maxarea:
                maxarea = s

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return maxarea
