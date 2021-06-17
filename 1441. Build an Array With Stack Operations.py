class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        target = str(''.join(map(str, target)))
        items = [i for i in range(1,n+1)]
        lis = []
        
        for i in items:
            if str(''.join(map(str, lis))) == target:
                break
            if len(lis)==0:
                lis.append(i)
                ans.append("Push")
                
                
            else:
                
                if not target.startswith(str(''.join(map(str, lis)))):
                    lis.pop(-1)
                    ans.append("Pop")
                    lis.append(i)
                    ans.append("Push")
                else:
                    lis.append(i)
                    ans.append("Push")
        return ans
