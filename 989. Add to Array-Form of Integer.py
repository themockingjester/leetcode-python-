class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        j = ""
        for i in A:
            j+=str(i)
        j = int(j)
        j+=K
        j=str(j)
        lis = []
        for i in j:
            lis.append(int(i))
        return lis
            
