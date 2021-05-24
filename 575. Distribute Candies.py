class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyTypes = list(set(candyType))
        maxAllowed = len(candyType) // 2
        if maxAllowed<=len(candyTypes):
            return maxAllowed
        else:
            return len(candyTypes)
