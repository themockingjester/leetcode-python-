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
