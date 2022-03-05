class Solution:
    def numSquares(self, n: int) -> int:
        def v1(n):
            nums,amount = [i*i for i in range(1,101) if i*i<=n],n
            # d={xx:xx//x for x in nums for xx in range(x,n+1,x)}
            ln,cache,c1,c2,mils =len(nums),{},0,0,[n]

            def combs(i,t,s):
                #if (i,t) in cache: return cache[(i,t)]
                #if cache.get(t,[-1,n])[0]>=i: return cache[t][1]
                # if cache.get(t,[n,n])[0]<=i: return cache[t][1]
                if t in cache: return cache[t]
                if s>=mils[-1]:return n
                else:
                    mi = n
                    if i<ln: 
                        for j in range(0,t//cnu[i]+1): 
                            if s+j>mils[-1]:break
                            p=j*cnu[i]
                            if t-p==0:
                                if j<mi:mi=j
                            elif t-p<0:break
                            else:
                                r = n  if j>=mi else  combs(i+1,t-p,s+j)
                                if  r+j<mi:mi=r+j
                    if t==n and mi<mils[-1]: mils.append(mi)
                    #cache[(i,t)]=mi
                    # cache[t]=(i,mi)
                    cache[t]=mi
                return mi


            cnu = sorted(nums,reverse=False)
            if n==1:return 1
            return combs(0,amount,0)
        #for n in range(9999,9998,-1):
        return v1(n)
