class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lis=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lis.append(matrix[i][j])
        lis=sorted(lis)
        return lis[k-1]
