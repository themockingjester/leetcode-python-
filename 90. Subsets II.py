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
