class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        filtered=[]
        toremove=[]
        setis = set(list(map(str, str(s))))
        # getting those characters whose occourances are less thsn k
        for i in setis:
            if s.count(i)<k:
                toremove.append(i)

        
        temp = ""
        # splitting s into a list such list wo'nt contain items of toremove list
        for i in s:
            if i in toremove:
                if len(temp)!=0:
                    filtered.append(temp)
                    temp=""
            else:
                temp+=i
        else:
            if len(temp)!=0:
                filtered.append(temp)
                temp=""
        
        maxlen = 0
        for i in filtered:
            if len(i)<k:
                continue
            s=i
            end=k
            previous = end
            ans=[]
            
            start=0
            while True:

                u = s[start:end]

                setis = set(list(map(str, str(u))))
                length = [i  for i in setis if u.count(i)>=k]
                if len(length)==len(setis):
                    if len(u)>maxlen:
                        maxlen=len(u)
                        start=0
                        previous+=1
                        end=previous
                        continue


                if len(u)==len(s):
                    break
                if end==len(s):
                    previous+=1
                    end=previous
                    start=0
                    continue
                end+=1
                start+=1
            
        return maxlen
