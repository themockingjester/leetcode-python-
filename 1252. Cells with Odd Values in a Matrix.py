class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        lis = []
        for i in range(m):
            k=[0 for p in range(n)]
            lis.append(k)
        
        for i in indices:
            
            for j in range(n):
                lis[i[0]][j]+=1
            
            for j in range(m):
                lis[j][i[1]]+=1
        ctr = 0
        for i in range(m):
            for j in range(n):
                if lis[i][j]%2!=0:
                    ctr+=1
        return ctr
