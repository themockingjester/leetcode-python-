class Solution:
    def toLowerCase(self, s: str) -> str:
        new=""
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                new+=chr(ord(i)+32)
                continue
            new+=i
        return new
