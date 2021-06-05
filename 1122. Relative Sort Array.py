class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lis = []
        for i in arr2:
            
            lis+=[i for j in range(arr1.count(i))]
            arr1 = [k for k in arr1 if k!=i]
            
        lis = lis+sorted(arr1)
        return lis
