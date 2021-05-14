class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = list(set(nums))
        for i in k:
            if nums.count(i)>len(nums)/2:
                return i
