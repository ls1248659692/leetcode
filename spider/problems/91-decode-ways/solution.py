class Solution:
    def __init__(self):
        self.d1 = [str(el) for el in range(1,10)]
        self.d2 = [str(el) for el in range(10,27)]
        self.cache={}
        self.cache.update({dd:1 for dd in self.d1})

    def numDecodings(self, s: str) -> int:
        r = 1
        len_s = len(s)
        if s in self.cache:return self.cache[s]
        if len_s==1:
            return 1 if  s in self.d1 else 0
        elif len_s==2:
            t2 = 1 if s[:2] in self.d2 else 0
            t1 = 1 if s[0] in self.d1 and s[1] in self.d1 else 0
            return t2+t1
        else:
            r1 = (r*self.numDecodings(s[1:])) if s[0] in self.d1 else 0
            r2 = (r*self.numDecodings(s[2:])) if s[:2] in self.d2 else 0
            r= r1+r2
        self.cache[s]=r
        #print(s,r)
        return r