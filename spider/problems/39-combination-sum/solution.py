class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combs(clis,t):
            r =[]
            if not clis: return [[]] if  t==0 else None
            for j in range(t//clis[0]+1):
                n1 = combs(clis[1:],t-j*clis[0])
                if n1: r+= [li+[clis[0]]*j for li in n1] 
            return r
        clis = sorted(candidates,reverse=True)
        return combs(clis,target)        