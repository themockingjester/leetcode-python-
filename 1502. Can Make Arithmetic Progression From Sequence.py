class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr)==1:
            return True
        arr = sorted(arr)
        diff = arr[1]-arr[0]
        for i in range(1,len(arr)):
            if(arr[i]-arr[i-1])==diff:
                pass
            else:
                return False
        else:
            return True
