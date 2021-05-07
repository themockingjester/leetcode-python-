class Solution:
    def findMin(self, nums: List[int]) -> int:
        k = nums
        k=sorted(k)
        return k[0]
