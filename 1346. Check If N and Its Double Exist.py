class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr2 = arr.copy()
        if(arr.count(0)==1):
            arr2 = [2*i for i in arr2 if i!=0]
        else:
            arr2 = [2*i for i in arr2]
        
        set1 = set(arr)
        set2=set(arr2)
        set3 = set.intersection(set1,set2)
        
        if len(set3)!=0:
            return True
        else:
            return False
        
