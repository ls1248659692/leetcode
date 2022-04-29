class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def v1(candidates,target):
            def combs(clis,t):
                r =[]
                if not clis: return [[]] if  t==0 else None
                for j in range(0,2):
                    n1 = combs(clis[1:],t-j*clis[0])
                    if n1: r+= [li+[clis[0]]*j for li in n1] 
                return r
            clis = sorted(candidates,reverse=True)
            r = combs(clis,target)        
            s = set([tuple(e) for e in r])
            return [list(e) for e in s]

        def v2(candidates,target):
            def cmb(n,t):
                if len(n)==0: return [[]] if t==0 else []
                s0= cmb(n[1:],t)
                s1= [[n[0]]+e for e in cmb(n[1:],t-n[0])]
                return [e for e in s0+s1 ]
            r= cmb(candidates,target) 
            s = set([tuple(sorted(e)) for e in r])
            return [list(e) for e in s]      

        def v3(candidates,target):
            from collections import Counter
            def combs(clis,t):
                r =[]
                if not clis: return [[]] if  t==0 else []
                #print(clis,t)
                for j in range(clis[0][1]+1):
                    if t-j*clis[0][0]>=0:
                        n1 = combs(clis[1:],t-j*clis[0][0])
                        if n1: r+= [li+[clis[0][0]]*j for li in n1] 
                return r
            clis = Counter(candidates).most_common()
            #print(clis)
            #clis = sorted(candidates,reverse=True)
            r = combs(list(clis),target)        
            return r
            #s = set([tuple(e) for e in r])
            #return [list(e) for e in s] 
                      
        return v3(candidates,target)
