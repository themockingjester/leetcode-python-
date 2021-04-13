class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lis = []
        ctr = 0
        data = ""
        found = False
        flag = False
        h = len(s)%k
        if h!=0:
            found = True
        for i in range(len(s)):
            ctr+=1
            data+=s[i]
            
            if ctr==k:
                if flag==False:
                    flag=True
                else:
                    flag = False
                lis.append(data)
                ctr=0
                data=""
        if found:
            lis.append(s[-1*h:])
        print(lis)
        ctr = 1
        j = ""
        for i in range(len(lis)):
            if ctr%2!=0:
                j+=str(lis[i])[::-1]
            else:
                j+=lis[i]
            ctr+=1
        print(j)
        return j
                
                
                
        
