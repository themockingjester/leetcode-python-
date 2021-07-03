class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lis = list(map(str, str(s)))
        rev = s[::-1]
        new=""
        for i in s:
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
                new+=i
        ctr=-1
        for i in range(len(lis)):
            if (ord(lis[i])>=65 and ord(lis[i])<=90) or (ord(lis[i])>=97 and ord(lis[i])<=122):
                lis[i]=new[ctr]
                ctr-=1
        return str(''.join(map(str, lis)))
                
