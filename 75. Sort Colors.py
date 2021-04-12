class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = sorted(nums)
        ctr=0
        for i in range(len(nums)):
            nums[i]=l[i]
