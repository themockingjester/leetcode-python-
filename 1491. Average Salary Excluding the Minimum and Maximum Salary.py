class Solution:
    def average(self, salary: List[int]) -> float:
        maxele = max(salary)
        minele = min(salary)
        ctr=0
        sumis=0
        for i in salary:
            if i not in [maxele,minele]:
                sumis+=i
                ctr+=1
        return sumis/ctr
                
