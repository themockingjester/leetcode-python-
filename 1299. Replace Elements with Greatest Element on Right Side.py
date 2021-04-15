class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i==len(arr)-1:
                arr[i]=-1
                break
            k = max(arr[i+1:])
            arr[i]=k
        return arr
            
