from  collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lis = []
        count = Counter(s)
        for i in s:
            count[i]-=1
            
            if i not in lis:
                while len(lis)!=0 and lis[-1]>i and count[lis[-1]]!=0:
                    lis.pop()
                lis.append(i)
            
        return "".join(lis)
