class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic ={}
        lis=[]
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            elif nums[i] in dic and dic[nums[i]]<2:
                dic[nums[i]]+=1
            else:
                lis.append(i)
        print(lis)
        ctr = 0
        for i in lis:
            print(i)
            del nums[i-ctr]
            ctr+=1
        print(nums)
        return len(nums)
