class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
        for i in rows:
            matrix[i][:]=[0 for k in range(len(matrix[0]))]
        for i in cols:
            for k in range(len(matrix)):
                matrix[k][i]=0
