class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis = []
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i])+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    lis.append(nums2[j])
                    break
            else:
                lis.append(-1)
        return lis
