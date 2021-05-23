class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        n=bin(n).replace("0b", "")
        print(n)
        return n.count('1')
