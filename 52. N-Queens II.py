class Solution:
    def checkVertically(self,cr,cc,rows,cols):
        while(cr>-1):
            
            if self.mat[cr][cc]==1:
                return False
            
            cr-=1
        return True
    def checkVerticallyLeft(self,cr,cc,rows,cols):
        while(cr>-1 and cc>-1):
            if self.mat[cr][cc]==1:
                return False
            cr-=1
            cc-=1
        return True
    def checkVerticallyRight(self,cr,cc,rows,cols):
        while(cr>-1 and cc<cols):
            if self.mat[cr][cc]==1:
                return False
            cr-=1
            cc+=1
        return True
    def move(self,cr,cc,rows,cols):
        for cc in range(cols):
            
            if self.checkVertically(cr-1,cc,rows,cols) and self.checkVerticallyLeft(cr-1,cc-1,rows,cols) and self.checkVerticallyRight(cr-1,cc+1,rows,cols):
                    
                self.mat[cr][cc]=1
                
                if cr==rows-1:
                    self.ctr+=1
                    # print(self.mat)
                    # print('----------------------------------')
                self.move(cr+1,0,rows,cols)
        
            
                self.mat[cr][cc]=0
    def totalNQueens(self, n: int) -> int:
        self.mat=[[0 for i in range(n)] for j in range(n)]
        
        self.ctr=0
        rows=len(self.mat)
        cols=len(self.mat[0])
        
        self.move(0,0,rows,cols)
        return self.ctr
        
                
        
