class Solution:

    def __init__(self, nums: List[int]):
        import random
        self.dic={}
        for i in range(len(nums)):
            
            if nums[i] in self.dic:
                self.dic[nums[i]].append(i)
            else:
                self.dic[nums[i]]=[i]

    def pick(self, target: int) -> int:
        t= random.randint(0,len(self.dic[target])-1)
        return self.dic[target][t]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
