class Solution(object):
    def subarraySum(self, nums, k):
    
        count = 0
        sumis=0
        dic={}
        dic[0]=1
        for i in range(len(nums)):
            sumis+=nums[i]
            count+=dic.get(sumis-k,0)
            dic[sumis]=dic.get(sumis,0)+1
        return count
