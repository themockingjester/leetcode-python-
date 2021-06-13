class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ele = 'a'
        result = False
        while True:
            if ele in sentence:
                result = True
                if ele == 'z':
                    return True
            else:
                return False
            ele = chr(ord(ele)+1)
            
