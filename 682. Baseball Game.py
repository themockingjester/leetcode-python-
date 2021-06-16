class Solution:
    def calPoints(self, ops: List[str]) -> int:
        lis = []
        for i in ops:
            if i not in ['+','D','C']:
                lis.append(int(i))
            else:
                if i=='+':
                    lis.append(lis[-1]+lis[-2])
                elif i=='D':
                    lis.append(2*lis[-1])
                elif i=='C':
                    lis.pop(len(lis)-1)
        return sum(lis)
