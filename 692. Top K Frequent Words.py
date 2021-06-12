class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        unique = set(words)
        dic={}
        for i in unique:
            if words.count(i) in dic:
                dic[words.count(i)].append(i)
            else:
                dic[words.count(i)]=[i]
        lis = sorted(dic.keys())[::-1]
        ans = []
        ctr=0
        for i in lis:
            for j in sorted(dic[i]):
                if ctr==k:
                    return ans
                    
                ctr+=1
                ans.append(j)
        return ans
