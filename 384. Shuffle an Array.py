class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.org = nums.copy()
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.org
        
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        dic = {}
        lis = []
        for i in range(len(self.arr)):
            while True:

                k = random.randrange(0, len(self.arr), 1)
                if k not in dic:
                    dic[k]=True
                    lis.append(self.arr[k])
                    break
        return lis
            
            
        
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
