class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = [i for i in s if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)]
        print(temp)
        s = str(''.join(map(str, temp)))
        print(s)
        s= s.lower()
        if s==s[::-1]:
            return True
        else:
            return False
