class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        def ckpar(s):
            while '()' in s: s=s.replace('()','')
            return s==''

        def rp(s):
            n = 0
            pn = []
            for i in range(len(s)):
                c= s[i]
                if c=='(':n+=1
                #pn.append(-n if s[i:i+2]==')(' or s[i-1:i+1]==')(' else n )
                pn.append(n )
                if c==')':n-=1
            return pn
        s = seq
        sli = list(s)
        parli =rp(s)
        print(s,parli)

        mx =max(parli)
        res = [0 if abs(p)>mx//2 else 1 for p in parli]   
        se0 =  ''.join([seq[i] for i in range(len(seq)) if res[i]==0])
        se1 =  ''.join([seq[i] for i in range(len(seq)) if res[i]==1])
        print(res,se0,se1,ckpar(se0),ckpar(se1),'
')       
        return res     

        #res= [1,1,0,0,0,0,1,1,0,0,0,0,1,1]
        for s in [se0,se1,seq]:
            sli = list(s)
            parli =rp(s)
            mx =max(parli)
            res_ = [0 if abs(p)==mx else 1 for p in parli]
            print(s,parli)
        return res