class Solution:
    def solve(self,n,lis,curr,arr):
        
        if len(lis)<=n:
            if str(lis) in self.dic:
                pass
            else:
                self.dic[str(lis)]=1
                self.res.insert(0,lis)
        else:
            return
        for i in range(curr,n):
            temp=lis.copy()
            temp.append(arr[i])
            self.solve(n,temp,i+1,arr)
        
    
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.dic={}
        self.res=[]
        self.solve(len(nums),[],0,sorted(nums))
        return self.res
# wit pure recursion
class Solution:
    def __init__(self):
        self.result=[]
        self.found={}
    def sol(self,index,currArr,nums,pattern):
        copiedArr = currArr.copy()
        if(pattern not in self.found):
            self.result.append(copiedArr)

        self.found[pattern]=True
        if(index>=len(nums)):  
            return
        
        # not pick
        self.sol(index+1,copiedArr,nums,pattern)

        #pick:
        copiedArr.append(nums[index])
        self.sol(index+1,copiedArr,nums,pattern+str(nums[index]))
        copiedArr.pop()
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.sol(0,[],nums,'')
        print(self.found)
        return self.result
