class Solution:
    def currentBoard(self,rows,cols):
        lis=[]
        
        for i in range(rows):
            s=""
            for j in range(cols):
                if self.mat[i][j]==1:
                    s+='Q'
                else:
                    s+='.'
            lis.append(s)
        self.lis.append(lis)
    def checkVertically(self,cr,cc,rows,cols):
        while cr!=-1:
            if self.mat[cr][cc]==1:
                return False
            cr-=1
        return True
    def verticallyLeftUp(self,cr,cc,rows,cols):
        while cr!=-1 and cc!=-1:
            if self.mat[cr][cc]==1:
                return False
            cr-=1
            cc-=1
        return True
    def verticallyRightUp(self,cr,cc,rows,cols):
        while cr!=-1 and cc!=cols:
            if self.mat[cr][cc]==1:
                return False
            cr-=1
            cc+=1
        return True
    def move(self,cr,cc,rows,cols):
        for cc in range(cols):
            if self.checkVertically(cr-1,cc,rows,cols) and self.verticallyRightUp(cr-1,cc+1,rows,cols) and self.verticallyLeftUp(cr-1,cc-1,rows,cols):
                self.mat[cr][cc]=1
                if cr==rows-1:
                    self.currentBoard(rows,cols)
                    
                self.move(cr+1,cc,rows,cols)
                self.mat[cr][cc]=0
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.lis=[]
        self.mat=[[0 for i in range(n)] for j in range(n)]
        rows=len(self.mat)
        cols=len(self.mat[0])
        self.move(0,0,rows,cols)
        return self.lis
