class Solution:
    def reverseVowels(self, s: str) -> str:
        j=[]
        k=[]
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                k.append(i)
                j.append('#*#')
            else:
                j.append(i)
        k=k[::-1]
        for i in range(len(s)):
            if len(k)!=0:
                if j[i]=="#*#":
                    j[i]=k[0]
                    del k[0]
            else:
                break
        return "".join(j)
