#  approach 1 without try and excpet faster than 68%
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows= len(mat)
        col = len(mat[0])
        
        for i in range(col):
            k=i
            lis=[]
            for j in range(rows):
                if k==col:
                    continue
                
                lis.append(mat[j][k])
                k+=1
            lis = sorted(lis)
            k=i
            ctr=0
            for j in range(rows):
                if k==col:
                    continue
                
                mat[j][k]=lis[ctr]
                k+=1
                ctr+=1
        for i in range(1,rows):
            lis=[]
            k=i
            u=0
            while k<rows and u<col:
            
                lis.append(mat[k][u])
                
                k+=1
                u+=1
            lis = sorted(lis)
            k=i
            u=0
            ctr=0
            while k<rows and u<col:
                
                mat[k][u]=lis[ctr]
                
                k+=1
                u+=1
                ctr+=1
            
        
        return mat
      
      # approach 2 only difference is in try and except fater than 98%
      class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows= len(mat)
        col = len(mat[0])
        
        for i in range(col):
            k=i
            lis=[]
            for j in range(rows):
                if k==col:
                    continue
                
                lis.append(mat[j][k])
                k+=1
            lis = sorted(lis)
            k=i
            ctr=0
            for j in range(rows):
                if k==col:
                    continue
                
                mat[j][k]=lis[ctr]
                k+=1
                ctr+=1
        for i in range(1,rows):
            lis=[]
            k=i
            u=0
            while k<rows:
                try:
                    lis.append(mat[k][u])
                except:
                    break
                k+=1
                u+=1
            lis = sorted(lis)
            k=i
            u=0
            ctr=0
            while k<rows:
                try:
                    mat[k][u]=lis[ctr]
                except:
                    break
                k+=1
                u+=1
                ctr+=1
            
        
        return mat
                
                
