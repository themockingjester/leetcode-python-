class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n!=0 and n% 2==0):
            n=n//2
        if n==1:
            return True
        else:
            return False
