class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ctr = 0
        x=bin(x).replace("0b", "")
        y=bin(y).replace("0b", "")
        len_x=len(x)
        len_y=len(y)
        if(len_x>len_y):
            for i in range(len_x-len_y):
                y = '0'+y
        elif (len_x<len_y):
            for i in range(len_y-len_x):
                x = '0'+x
        
        else:
            pass
        
        
        print(x,y)
        for i in range(len(x)):
            if x[i]!=y[i]:
                ctr+=1
        return ctr
