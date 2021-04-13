class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split(" ")
        lis=[]
        for i in range(len(k)):
            lis.append((k[i])[::-1])
        return " ".join(lis)
        
