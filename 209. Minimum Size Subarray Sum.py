class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0 
        window_sum = 0
        minimum = 10 ** 10000
        
        while end < len(nums):
            if window_sum < target:
                window_sum += nums[end]
                end += 1
            while window_sum >= target:
                if end - start < minimum:
                    minimum = end - start
                window_sum -= nums[start]
                start += 1
                
        if minimum == 10 ** 10000:
            return 0
        else:
            return minimum
            
            
