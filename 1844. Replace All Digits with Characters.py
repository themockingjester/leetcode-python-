class Solution:
    def replaceDigits(self, s: str) -> str:
        s2 = ""
        for i in range(0,len(s)):
            if s[i] in ['1','2','3','4','5','6','7','8','9','0']:
                s2+=chr(ord(s[i-1])+int(s[i]))
            else:
                s2+=s[i]
        return s2
