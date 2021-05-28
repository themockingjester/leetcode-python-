class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ctr=0
        for i in range(len(strs[0])):
            arr = []
            for j in range(len(strs)):
                arr.append(strs[j][i])
            k = sorted(arr)
            if k != arr:
                ctr+=1
        return ctr
