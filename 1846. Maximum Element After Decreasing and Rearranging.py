class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        if arr[0]==1:
            for i in range(1,len(arr)):
                if abs(arr[i]-arr[i-1])<=1:
                    pass
                else:
                    arr[i]=arr[i-1]+1
        else:
            ctr=1
            for i in range(len(arr)):
                arr[i]=ctr
                ctr+=1
        return max(arr)
                
