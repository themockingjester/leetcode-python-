class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        first=nums.index(target)
        last = nums[::-1].index(target)+1
        last = len(nums)-last
        return [first,last]
