class Solution:
    def checkSubGrid(self,lis):
        for i in range(0,7,3):
            v=0
            for j in range(0,3):
                
                lis2=[]
                u=i
                
                for k in range(9):
                    if lis[u][v]!=".":
                        
                        lis2.append(lis[u][v])
                    u+=1
                    if u==i+3:
                        u=i
                        v+=1
                
                if len(lis2)!=len(set(lis2)):
                    return False
                
               
        return True

    def checkColumnsAndRows(self,lis):
        for i in range(9):
            lis2=[]
            for j in range(9):
                if lis[i][j]!=".":
                    lis2.append(lis[i][j])
                    
            if len(lis2)==len(set(lis2)):
                pass
            else:
                return False
            lis2=[]
            for j in range(9):
                if lis[j][i]!=".":
                    lis2.append(lis[j][i])
                    
            if len(lis2)==len(set(lis2)):
                pass
            else:
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.checkColumnsAndRows(board):
            
            if self.checkSubGrid(board):
                
                return True
            else:
                return False
        else:
            return False
            
