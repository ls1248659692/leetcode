class Solution:
    def countPrimes(self, n: int) -> int:
        pli = [ 2,3,5,7]
        cn =4
        for i in range(9,3000,2):
            sq = int(i**0.5)+1
            for p in pli:
                if p >sq:
                    cn+=1
                    pli.append(i)
                    break
                if i%p==0:
                    break
        p3k=list(pli)
        if n<=3000: return len([e for e in p3k if e<n])
        if n>400*1000*1000: return -1
        dic_p = {k:1 for k in range(3001,n)}
        for i in range(len(p3k)):
            for j in range(2,n//p3k[i]+1):
                dic_p[j*p3k[i]]=0
        cn = len(p3k) + len([e for e in dic_p.values() if e==1] )
        return cn
        