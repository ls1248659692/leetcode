class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        s = s.replace('()','+1')
        s = s.replace('(+1)','+2')

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

        print(s)
        if ')' not in s:
            return int(eval(s))
        else:
            while '(' in s:
                while ')(' in s: s=s.replace(')(',')+0+(')
                #s= s.replace('()','+1').replace('(+1)','+2')
                sli = list(s)
                parli =rp(s)
                mx = max(parli)         
                dli = [i for i in range(len(parli)) if parli[i] in [mx]] 
                
                psli = psplit(dli)
                print('parli%s dli=%s psli=%s,mx=%s s=%s sli=%s'%(parli,dli,psli,mx,s,sli))   
                for b,e in psli:
                    #if s[e]!=')' and s[e+1]==')' and parli[e+1]==-1: e =e+1
                    print(s[b:e+1],sli[b:e+1])
                    v = '+%s'%(2*eval(s[b+1:e]))
                    v += ' '*(e+1-b-len(v)) 
                    print(len(sli[b:e+1]),len(v))
                    sli[b:e+1] = v       
                s= ''.join(sli).replace(' ','')
                print('psli=%s,r=%s'%(psli,s))            
            return int(eval(s))
       