class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums=sorted(nums)
        return min((abs(nums[0]-nums[-4]),abs(nums[1]-nums[-3]),abs(nums[2]-nums[-2]),abs(nums[3]-nums[-1]))) if len(nums)>3 else 0
