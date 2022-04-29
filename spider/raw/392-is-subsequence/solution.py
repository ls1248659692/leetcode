class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @lru_cache
        def subs(ss,ts):
            if len(ss)==1 : return [('',ts[ts.index(ss[0])+1:])] if ss[0] in ts else []
            elif len(ss)>=2:
                for i in range(len(ts)):
                    if ts[i]==ss[0]:
                        t= subs(ss[1:],ts[i+1:])
                        if t:    return t
            return []

        ss,ts =list(s),[ e for  e in list(t) if e in set(list(s))]
        return len([tt for tt in subs(''.join(ss),''.join(ts)) if not tt[0]])!=0 if ss else True