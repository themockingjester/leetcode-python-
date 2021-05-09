class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lis = []
        ctr=0
        for i in nums:
            ctr+=i
            lis.append(ctr)
        return lis
