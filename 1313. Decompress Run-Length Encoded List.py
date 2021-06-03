class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        times = len(nums)//2
        print(times)
        arr = []
        ctr=0
        g = 0
        k=1
        while ctr<times:
            ctr+=1
            arr2 = [nums[k] for i in range(nums[g])]
            arr.extend(arr2)
            k+=2
            g+=2
        return arr
