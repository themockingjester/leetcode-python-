class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        universal = nums[0]
        for i in nums[1:]:
            curr_max,curr_min = max(i,curr_max*i,curr_min*i),min(i,curr_max*i,curr_min*i)
            universal = max(universal,curr_max)
        return universal
