class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ctr=1
        while True:
            if ctr not in nums:
                return ctr
            ctr+=1
