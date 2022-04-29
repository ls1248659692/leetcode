class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s,goal = s1,s2
        cs = set(list(s))
        if len(s)!=len(goal) or sorted(list(s))!=sorted(list(goal)):return False
        dli = [s[i] for i in range(len(s)) if s[i]!=goal[i]]
        print(dli)
        if len(dli)==0: return  True
        elif len(dli)==1: return False
        elif len(dli)==2: return True
        else: return False        