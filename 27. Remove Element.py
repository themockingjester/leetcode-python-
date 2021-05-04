class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lis = []
        start = 0
        end = len(nums)-1
        for i in range(len(nums)):
            if nums[i]==val:
                lis.append(i)
        ctr=0
        for i in lis:
            del nums[i-ctr]
            ctr+=1
            
