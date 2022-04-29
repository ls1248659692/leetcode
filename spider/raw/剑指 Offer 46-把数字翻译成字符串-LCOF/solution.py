class Solution:
    def __init__(self):
        self.d1 = [str(el) for el in range(10)]
        self.d2 = [str(el) for el in range(10,26)]
        self.cache ={}
        self.cache.update({kk:1 for kk in self.d1})

    def t_num(self,pstr):
        #print('t_num',pstr)
        if pstr in self.cache:return self.cache[pstr]
        if len(pstr)==1:
            r= 1
        elif len(pstr)==2:
            r= 2 if pstr in self.d2 else 1
        else:
            r1 = self.t_num(pstr[1:])
            r2 = self.t_num(pstr[2:]) if pstr[:2] in self.d2 else 0
            r = r1+r2
        self.cache[pstr]=r
        return r

    def translateNum(self, num: int) -> int:
        return self.t_num(str(num))