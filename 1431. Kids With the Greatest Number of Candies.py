class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        lis=[]
        for i in candies:
            if i + extraCandies >= maxi:
                lis.append(True)
            else:
                lis.append(False)
        return lis
