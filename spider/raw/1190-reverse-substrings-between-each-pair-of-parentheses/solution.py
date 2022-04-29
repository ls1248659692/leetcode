class Solution:
    def reverseParentheses(self, s: str) -> str:
        def rp(s):
            n = 0
            pn = []
            for i in range(len(s)):
                c= s[i]
                if c=='(':n+=1
                pn.append(-n if s[i:i+2]==')(' or s[i-1:i+1]==')(' else n )
                if c==')':n-=1
            return pn

        def psplit(li):
            rli = [ [li[0],li[0]] ]
            for e in li[1:]:
                if e!=rli[-1][-1]+1: rli.append([e,e])
                else: rli[-1][-1]=e
            return rli

        while '()' in s: s= s.replace('()','')
        print(s)
        while '(' in s:
            s= s.replace('()','')
            sli = list(s)
            parli =rp(s)
            
            mx = max(parli)
            dli = [i for i in range(len(parli)) if parli[i] >=mx ]
            psli = psplit(dli)
            print('parli%s dli=%s psli=%s'%(parli,dli,psli)) 

            for b,e in psli:
                sli[b:e+1]= ['.' if el in')(' else el for el in sli[b:e+1][::-1]]
            for j  in range(len(parli)):  sli[j]='.' if parli[j]==-mx else sli[j]
                
            s= ''.join(sli).replace('.','')
            print('psli=%s,r=%s'%(psli,s))

        return s
