class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumis=0
        for i in nums[0:k]:
            sumis+=i
        result = sumis
        for i in range(k,len(nums)):
            sumis+=nums[i]-nums[i-k]
            result=max(result,sumis)
        return result/k
