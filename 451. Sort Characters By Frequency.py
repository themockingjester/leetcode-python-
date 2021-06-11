class Solution:
    def frequencySort(self, s: str) -> str:
        unique = set(list(map(str, str(s))))
        dic={}
        for i in unique:
            if s.count(i) in dic:
                dic[s.count(i)].append(i)
            else:
                dic[s.count(i)]=[i]
        lis = sorted(dic.keys())[::-1]
        ans = ""
        for i in lis:
            for j in dic[i]:
                temp=j*i
                ans+=temp
        return ans
