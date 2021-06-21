class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if i==len(matrix)-1:
                if target in matrix[i]:
                    return True
                else:
                    return False
            if target>=matrix[i][0] and target<matrix[i+1][0]:
                if target in matrix[i]:
                    return True
        else:
            return False
