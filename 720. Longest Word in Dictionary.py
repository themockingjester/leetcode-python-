class Solution:
    def longestWord(self, words: List[str]) -> str:
        maxi = 0
        
        dic= {}
        for i in words:
            
            for j in range(len(i)-1):
                
                if i[0:j+1] not in words:
                    break
            else:
                if len(i) not in dic:
                    dic[len(i)]=[i]
                else:
                    dic[len(i)].append(i)
                if len(i)>maxi:
                    maxi = len(i)
                    
        
        if len(dic)==0:
            return ""
        return sorted(dic[maxi])[0]
                
