class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        mi = str1 if len(str1)<len(str2) else str2
        ma = str1 if len(str1)>=len(str2) else str2
        x = mi
        while x and (ma.replace(x,'')!='' or mi.replace(x,'')!='') :
            x = x[1:]
        return x