class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        lis = s.split(" ")
        
        lis=lis[::-1]
        print(lis)
        temp = [i for i in lis if i!=""]
        new=" ".join(temp)
        return new
