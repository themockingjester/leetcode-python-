class Solution:
    def minOperations(self, logs: List[str]) -> int:
        lis = []
        for i in logs:
            if i == "../":
                if len(lis)!=0:
                    lis.pop(-1)
            elif i=="./":
                pass
            else:
                lis.append(i)
        return len(lis)
