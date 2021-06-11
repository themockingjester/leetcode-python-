class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = set(nums)
        dic={}
        for i in unique:
            if nums.count(i) in dic:
                dic[nums.count(i)].append(i)
            else:
                dic[nums.count(i)]=[i]
        lis = sorted(dic.keys())[::-1]
        ans = []
        ctr=0
        for i in lis:
            for j in dic[i]:
                if ctr==k:
                    return ans
                    
                ctr+=1
                ans.append(j)
        return ans
