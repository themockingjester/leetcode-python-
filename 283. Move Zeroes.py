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
        
