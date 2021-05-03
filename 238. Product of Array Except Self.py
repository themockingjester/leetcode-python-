# concept taken  from youtube channel nickwhite
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0 for i in nums]
        left[0]=1
        right = [0 for i in nums]
        right[-1]=1
        for i in range(1,len(left)):
            left[i]=nums[i-1]*left[i-1]
            
        for i in range(len(right)-1,0,-1):
            right[i-1]=nums[i]*right[i]
        lis=[]
        print(left,right)
        for i in range(len(left)):
            lis.append(left[i]*right[i])
        return lis
