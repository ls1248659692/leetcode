class Solution:
    def maxProfit(self, pr: List[int]) -> int:
        #@lru_cache
        def mmsubseq(nums,l,r,mx_mi='max',isgreedy=False):
            #print('...',nums[l:r])
            if l>=r:return 0,None,None
            _mmb,mmb,mme = l-1,l-1,l-1
            c, cdiffm,cleftm=0,0,0
            for i in range(l,r):
                n= nums[i]
                if mx_mi=='max':
                    if c+n<cleftm:_mmb=i
                    if c+n-cleftm>cdiffm:mmb,mme=_mmb,i
                    c,cleftm,cdiffm = c+n,min(c+n,cleftm),max(cdiffm,c+n-cleftm)
                else:
                    if c+n>cleftm:_mmb=i
                    if c+n-cleftm<cdiffm:mmb,mme=_mmb,i
                    c,cleftm,cdiffm = c+n,max(c+n,cleftm),min(cdiffm,c+n-cleftm)
                #print(c,cleftm,cdiffm)
            return cdiffm,mmb+1,mme+1 #withL withoutR

        if len(pr)<2:return 0
        lefmi = [float('inf')]
        for p in pr: lefmi.append(min(p,lefmi[-1]))

        #print(lefmi,'
',pr)
        mxp= max(pr[i]-lefmi[i]for i in range(len(pr)))
        chgli = [pr[i]-pr[i-1] for i in range(1,len(pr))]

        #chgli= [e for i,e in enumerate(chgli) if not (e==0 and chgli[i-1]==0 )]
        print(chgli)
        ln=len(chgli)
        mx1,mx1b,mx1e=mmsubseq(tuple(chgli),0,ln,'max',True)
        # mx2,mx2b,mx2e=maxsubseq(tuple(chgli[::-1]),0,ln,False)
        # mx2b,mx2e=ln-1-mx2e,ln-1-mx2b
        print('mx1=%s %s %s'%(mx1,mx1b,mx1e),chgli[mx1b:mx1e])
        #
        split= mx1b
        if chgli[mx1b:mx1e]:
            mx2,mx2b,mx2e=mmsubseq(tuple(chgli[mx1b:mx1e]),0,mx1e-mx1b,'min',False)
            print('raw_mx2',mx2,mx2b,mx2e,'mx1b=%s'%mx1b)
            mx2b,mx2e= mx1b+mx2b, mx1b+mx2e
            print('adj_mx2',mx2,mx2b,mx2e,chgli[mx1b:mx1e])
            if mx2b!=mx2e and mx2b>mx1b: split=mx2b  
        mxp2= mmsubseq(tuple(chgli),0,split)[0]+mmsubseq(tuple(chgli),split,ln)[0]
        mxp1= mmsubseq(tuple(chgli),0,mx1b)[0]+mmsubseq(tuple(chgli),mx1b,ln)[0]
        mxp3= mmsubseq(tuple(chgli),0,mx1e)[0]+mmsubseq(tuple(chgli),mx1e,ln)[0]
        return max([0,mxp2,mxp1,mxp3])