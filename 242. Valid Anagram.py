class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s = sorted(list(map(str, str(s))))
            
            t = sorted(list(map(str, str(t))))
            if s==t:
                return True
        
        return False
