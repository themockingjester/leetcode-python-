class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs=sorted(costs)
        ctr=0
        ans = 0
        for i in costs:
            if ctr+i<=coins:
                ctr=ctr+i
                ans+=1
            else:
                break
        return ans
