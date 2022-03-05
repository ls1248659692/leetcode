class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def echo(ss):
            if ss in c2:return c2[ss]
            if len(ss)==1:
                 res=True
            else:
                res =True
                for ii in range(1, len(ss) // 2 + 1):
                    if ss[ii - 1] != ss[-ii]:
                        res=False
                        break
            c2[ss]=res
            return res

        def pt_v0(s):
            #if len(cache)>=11: return set()
            if s in cache: return cache[s]
            if len(s)==1: res= set([tuple([s,])])
            elif len(s)==2: 
                res = set([(s[0],s[1])])
                res = res.union( set([tuple([s,])]) if echo(s) else set())
            else:
                p0 =  set([tuple([s,])]) if echo(s) else set()
                p3 = set()

                for j in range(1,len(s)):
                    s1,s2=s[:j],s[j:]
                    #print('s=%s,s1=%s,pts1=%s,s2=%s,pts2=%s'%(s,s1,pt(s1),s2,pt(s2)))
                    for pt1 in pt(s1):
                        for pt2 in pt(s2):
                            p3.add( tuple(pt1 + pt2))

                res= p0.union(p3)
            cache[s]=res
            return res

        def pt(s):
            #if len(cache)>=11: return set()
            if s in cache: return cache[s]
            if len(s)==1: res= set([s])
            elif len(s)==2: 
                res = set([s[0]+'.'+s[1]])
                res = res.union( set([s]) if echo(s) else set())
            else:
                p0 =  set([s]) if echo(s) else set()
                p3 = set()
                for j in range(1,len(s)):
                    for pt1 in pt(s[:j]):
                        for pt2 in pt(s[j:]):
                            p3.add( pt1 + '.'+pt2)

                res= p0.union(p3)
            cache[s]=res
            return res

        cache={}
        c2={}
        print(len(s))
        res= pt(s)
        print(len(res),len(c2),len(cache))
        res = [e.split('.') for e in  res]
        return res
