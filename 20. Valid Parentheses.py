class Solution:
    def isValid(self, s: str) -> bool:
        must = []
        
        close = [']',')','}']
        for i in s:
            if i in close:
                if len(must)!=0:
                    if i == must[-1]:
                        must.pop()
                    else:
                        return False
                else:
                    return False
            elif i == '{':
                must.append('}')
            elif i == '[':
                must.append(']')
            elif i == '(':
                must.append(')')
        print(must)
        if len(must)==0:
            return True
            
            
                
