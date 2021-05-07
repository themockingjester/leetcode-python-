class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lis=[]
        start=0
        end=len(nums)-1
        while start<=end:
            if start==end:
                if nums[start] in lis:
                    lis.remove(nums[start])
                else:
                    lis.append(nums[start])
            if nums[start] in lis:
                lis.remove(nums[start])
            else:
                lis.append(nums[start])
            if nums[end] in lis:
                lis.remove(nums[end])
            else:
                lis.append(nums[end])
            start+=1
            end-=1
        return lis[0]
