class Solution:
    def distance(self,x1,y1,x2,y2):
        return pow(((x2-x1)**2+(y2-y1)**2),0.5)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic={}
        for i in points:
            dis = self.distance(i[0],i[1],0,0)
            if dis in dic:
                dic[dis].append(i)
            else:
                dic[dis]=[i]
        ans=[]
        ctr=0
        print(dic)
        for i in sorted(dic.keys()):
            for j in dic[i]:
                if ctr==k:
                    return ans
                ans.append(j)
                ctr+=1
        return ans
                
                
