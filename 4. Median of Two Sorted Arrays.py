class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1+nums2
        arr= sorted(arr)
        if len(arr)%2!=0:
            return arr[len(arr)//2]
        else:
            k = len(arr)//2
            print(arr[k-1]+arr[k])
            return ((arr[k-1]+arr[k])/2)
