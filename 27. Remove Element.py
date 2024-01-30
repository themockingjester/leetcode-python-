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

# Another
# Space- O(N)
# Time - O(N)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        different=0
        while i<len(nums):
            if(nums[i]!=val):
                different+=1
                i+=1
            else:
                nums
        return different
            
