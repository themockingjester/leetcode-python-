class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lis= sentence.split(" ")
        ctr=1
        for i in range(len(lis)):
            if lis[i][0] in ['A','E','I', 'O','U','a','e','i','o','u']:
                lis[i] = lis[i]+'ma'+('a'*ctr)
            else:
                lis[i] = lis[i][1:]+lis[i][0]+'ma'+('a'*ctr)
            ctr+=1
        return " ".join(lis)
