class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis = s.split(" ")
        print(lis)
        if len(lis)==0:
            return 0
        else:
            lis = [i for i in lis if i != ""]
            if len(lis)==0:
                
                return 0
            return len(lis[-1])
