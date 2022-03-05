class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        pli = sorted(properties,key=lambda xx:xx[0])
        rli = {}
        for a,d in pli:
            rli.setdefault(a,[])
            rli[a].append(d)
        rli = {a:sorted(rli[a],reverse=True) for a in rli}
        st = sorted(rli.items(),key=lambda xx:xx[0],reverse=True)

        mxd = st[0][1][0]
        r=0
        print(st,mxd)
        for a,dli in st[1:]:
            print(a,r,mxd)
            r+=sum(1 for d in dli if d<mxd)
            mxd = max(dli[0],mxd)

        # mxli = [(a,dli[-1]) for a,dli in st][::-1]
        # r=0
        # for i in range(len(pli)):
        #     a,d = pli[i]
        #     for mxa,mxd in mxli:
        #         if a<mxa and d<mxd:
        #             r+=1
        #             break
        #         if a>=mxa:
        #             break
        return r