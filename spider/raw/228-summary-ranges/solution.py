class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        tn =[-99999] + nums+[-99999]
        sp=[(tn[i-1],tn[i]) for i in range(1,len(tn)) if tn[i]-tn[i-1]-1!=0]
        spb= [e for r in sp for e in r][1:-1]
        print (spb)
        spc = ['%s'%spb[i] if spb[i]==spb[i+1] else '%s->%s'%(spb[i],spb[i+1]) for i in range(0,len(spb),2)]
        print(spc)
        return spc