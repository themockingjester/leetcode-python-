class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lis = []
        k = list(set(nums))
        for i in k:
            if nums.count(i)>len(nums)/3:
                lis.append(i)
        return lis
        
