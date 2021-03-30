class Solution:
    def firstUniqChar(self, s: str) -> int:
        z = set()
        for i in range(len(s)):
            if s[i] not in z:
                k = s.count(s[i])
                if k==1:
                    return i
                else:
                    z.add(s[i])
        return -1
