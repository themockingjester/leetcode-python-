class Solution:
    def entityParser(self, text: str) -> str:
        
        check=["&quot;","&apos;","&amp;","&gt;","&lt;","&frasl;"]
        toReplace=["\"","'","&",">","<","/"]
        
        for i in check:
            text=text.replace(i,toReplace[check.index(i)]+"___",9999999999999)
        return text.replace('___',"",9999999)
