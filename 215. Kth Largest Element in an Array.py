class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        nums = nums[::-1]
        return nums[k-1]
