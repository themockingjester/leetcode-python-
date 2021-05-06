class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis = []
        dic={}
        if len(nums1)<=len(nums2):
            for i in nums1:
                if i in nums2 and i not in dic:
                    dic[i]=1
                    k=nums1.count(i)
                    l=nums2.count(i)
                    if k<= l:
                        while k!=0:
                            lis.append(i)
                            k-=1
                    else:
                        while l!=0:
                            lis.append(i)
                            l-=1
                        
        else:
            for i in nums2:
                if i in nums1 and i not in dic:
                    dic[i]=1
                    k=nums1.count(i)
                    l=nums2.count(i)
                    if k<= l:
                        while k!=0:
                            lis.append(i)
                            k-=1
                    else:
                        while l!=0:
                            lis.append(i)
                            l-=1
        return lis
