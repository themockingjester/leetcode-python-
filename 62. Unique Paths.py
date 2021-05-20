class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lis=[]
        newarr=[]
        if n==1:
            return 1
        for i in range(m):
            lis.clear()
            for j in range(n):
                lis.append(0)
            newarr.append(lis)
        for i in range(1,n):
            newarr[0][i]=1
        
        for i in range(1,m):
            newarr[i][0]=1
        for i in range(1,m):
            for j in range(1,n):
                newarr[i][j]=newarr[i-1][j]+newarr[i][j-1]
        return newarr[m-1][n-1]
