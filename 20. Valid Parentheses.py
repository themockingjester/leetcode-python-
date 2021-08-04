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
      
                                            # Another Approach (Easy and Faster)
class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        dic={
            ')':'(',
            '}':'{',
            ']':'[',
        }
        for i in s:
            if i==')' and len(arr)!=0 and arr[-1]==dic[')']:
                arr.pop()
            elif i=='}' and len(arr)!=0 and arr[-1]==dic['}']:
                arr.pop()
            elif i==']' and len(arr)!=0 and arr[-1]==dic[']']:
                arr.pop()
            else:
                arr.append(i)
        
        if len(arr)==0:
            return True
        else:
            return False
            
            
                
            
            
                
