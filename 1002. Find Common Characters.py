class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        previous = list(map(str, str(words[0])))
        for i in range(1,len(words)):
            lst2 = list(map(str, str(words[i])))
            temp = []
            t2 = previous.copy()
            for i in t2:
                if i in lst2:
                    lst2.pop(lst2.index(i))
                else:
                    previous.pop(previous.index(i))
        return previous
