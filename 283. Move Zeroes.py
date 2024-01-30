class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        lis=[]
        lis2=[]
        end = len(nums)-1
        for i in nums:
            if i==0:
                lis2.append(0)
            else:
                lis.append(i)
        
        
        nums[:] = lis[:]+lis2[:]

# Another solution 
# time - O(n)
# space - O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if(len(nums)<2):
            pass
        else:
            i = 0
            j=i+1
            while(j<len(nums)):
                if(nums[i]==0 and nums[j]!=0):
                    temp = nums[j]
                    nums[j]=nums[i]
                    nums[i] = temp
                    i+=1
                elif(nums[i]==0 and nums[j]==0):
                    j+=1;
                else:
                    i+=1
                    j+=1

        
