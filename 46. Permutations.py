class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import math,random
        times = math.factorial(len(nums))
        
        lis = []
        dic={}
        for i in range(times):
        
            while True:
                p = str(''.join(map(str, nums)))
                if p in dic:
                    random.shuffle(nums)
                else:
                    dic[p]=1
                    lis.append(nums.copy())
                    break
        
            
        return lis
