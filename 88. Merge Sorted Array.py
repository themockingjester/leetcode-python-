class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = nums1
        ctr=len(nums1)-1
        for i in nums2:
            nums1.pop(ctr)
            nums1.append(i)
            ctr-=1
        nums1.sort()
        
