class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def clr(left,right):
            d={}
            for i in range(left,right):
                c=s[i]
                d.setdefault(c,[])
                d[c].append(i)
            return d.items()

        def out(it,left,right):
            t = []
            n_it=[]
            for c,li in it:
                tli = [e for e in li if left<=e<right]
                n_it.append((c,tli))
                if len(tli)>=2: t.append((c,tli[0],tli[-1]))

            if not t: return [],[]
            t = sorted(t,key=lambda xx:xx[1])
            min_r = t[0][-1]
            ou=[t[0]]
            for i in range(1,len(t)):
                if t[i][-1]<min_r: 
                    min_r= t[i][-1]
                else:
                    ou.append(t[i])
            return ou,n_it

        def lop(it,left,right):# [left,right)
            if right-left==0:return 0
            if (left,right) in cache:return cache[(left,right)]
            ou,it = out(it,left,right)
            res= max([lop(it,i+1,j) if j>i else 0 for c,i,j in ou ])+2 if ou else 1
            cache[(left,right)]=res
            return res
        cache={}
        ou,it =out(clr(0,len(s)),0,len(s))
        mx= lop(it,0,len(s))
        return mx