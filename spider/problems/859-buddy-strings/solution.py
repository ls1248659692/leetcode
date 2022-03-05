class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        cs = set(list(s))
        if len(s)!=len(goal) or sorted(list(s))!=sorted(list(goal)):return False
        dli = [s[i] for i in range(len(s)) if s[i]!=goal[i]]
        print(dli)
        if len(dli)==0: return  max([s.count(c) for c in cs ])>=2
        elif len(dli)==1: return False
        elif len(dli)==2: return True
        else: return False