class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def v3(candidates,target,k):
            from collections import Counter
            def combs(clis,t):
                r =[]
                if not clis: return [[]] if  t==0 else []
                for j in range(clis[0][1]+1):
                    if t-j*clis[0][0]>=0:
                        n1 = combs(clis[1:],t-j*clis[0][0])
                        if n1: r+= [li+[clis[0][0]]*j for li in n1] 
                return r
            clis = Counter(candidates).most_common()
            r = combs(list(clis),target)        
            return [ls for ls in r if len(ls)==k]
                      
        return v3([e for e in range(1,10)],n,k)        