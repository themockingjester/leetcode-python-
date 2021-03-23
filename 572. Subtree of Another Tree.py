class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ctr = 0
        for i in items:
            if ruleKey == "type" and ruleValue == i[0]:
                ctr+=1
            elif ruleKey == "color" and ruleValue == i[1]:
                ctr+=1
            elif ruleKey == "name" and ruleValue == i[2]:
                ctr+=1
        return ctr
