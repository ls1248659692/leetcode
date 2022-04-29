class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        def v1(n,trust):
            ter=set([t[0] for t in trust])
            tee=set([t[1] for t in trust])
            tli = [t[1] for t in trust]
            teem = { t:tli.count(t) for t in tee}
            teemx = {t:num for t,num in teem.items() if num==n-1}
            cz=set(list(range(1,n+1)))
            c1 = cz-ter
            c2 = c1&tee
            print('not er',c1,'be trusted',c2,'max trusted',teemx)
            lc2= list(c2)
            if n==1: return 1  if trust==[] else -1
            return lc2[0] if len(lc2)==1 and lc2[0] in teemx else -1
        return v1(n,trust)

        def v0(n,trust):
            ter=set([t[0] for t in trust])
            tee=set([t[1] for t in trust])
            cz=set(list(range(1,n+1)))
            c1 = cz-ter
            c2 = c1&tee
            print(c2)
            return list(c2)[0] if len(c2)==1 else -1            
        return v0(n,trust)