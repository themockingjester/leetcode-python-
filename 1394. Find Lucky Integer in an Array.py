class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arrnew = []
        arrset=list(set(arr))
        for i in arrset:
            if arr.count(i)==i:
                arrnew.append(i)
        if len(arrnew)==0:
            return -1
        else:
            return max(arrnew)
            
