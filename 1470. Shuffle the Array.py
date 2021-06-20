class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[0:n]
        
        lis=[]
        second = nums[n:]
        for i in range(n):
            lis.extend((first[i],second[i]))
        return lis
