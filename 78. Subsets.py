class Solution:
    def solve(self,n,lis,curr,arr):
        
        if len(lis)<=n:
            self.res.insert(0,lis)
        else:
            return
        for i in range(curr,n):
            temp=lis.copy()
            temp.append(arr[i])
            self.solve(n,temp,i+1,arr)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.solve(len(nums),[],0,nums)
        return self.res

# With pure recursion
class Solution:
    def __init__(self):
        self.result=[]
        self.found={}
    def subsetsSol(self,index,currArr,nums):

        copiedArr = currArr.copy()
        if index>= len(nums):
            self.result.append(copiedArr)
            return
        # pick
        copiedArr.append(nums[index])
        self.subsetsSol(index+1,copiedArr,nums)
        copiedArr.pop()

        # not pick
        self.subsetsSol(index+1,copiedArr,nums)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsetsSol(0,[],nums)
        return self.result
