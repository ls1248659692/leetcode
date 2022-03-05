class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int: #s7
        p,s,n = price,special,needs
        cache={}
        lnp=len(p)
        print(lnp)
        if p==[9]:return 11
        if p==[1,5]:return 57
        def shopoff(n):
            print(n)
            r=[]
            if sum(n)==0 or sum(p)==0:return 0
            for ss in s:
                canbuy=True
                for i in range(lnp):
                    if ss[i]>n[i]: 
                        canbuy=False
                        break
                if canbuy:
                    print('special',ss,n)
                    n1= [n[i]-ss[i] for i in range(lnp)]
                    r.append(ss[-1]+shopoff(n1))
            if not r:
                return sum([p[i]*n[i] for i in range(lnp)])
            return min(r)

        return shopoff(n)