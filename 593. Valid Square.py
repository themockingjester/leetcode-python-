class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1==p2 or p2==p3 or p3==p4 or p4==p1 or p1==p3 or p4==p2:
            return False
        d1=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
        d2=pow((p2[0]-p3[0])**2+(p2[1]-p3[1])**2,0.5)
        d3=pow((p3[0]-p4[0])**2+(p3[1]-p4[1])**2,0.5)
        d4=pow((p1[0]-p4[0])**2+(p1[1]-p4[1])**2,0.5)
        dia1=pow((p1[0]-p3[0])**2+(p1[1]-p3[1])**2,0.5)
        dia2=pow((p2[0]-p4[0])**2+(p2[1]-p4[1])**2,0.5)
        setis = set()
        setis.add(d1)
        setis.add(d2)
        setis.add(d3)
        setis.add(d4)
        setis.add(dia2)
        setis.add(dia1)
        
        
        print(setis)
        if(len(setis)==2):
            return True
        else:
            return False
