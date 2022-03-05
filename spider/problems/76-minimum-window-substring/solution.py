class Solution:
    def minWindow(self, s: str, t: str) -> str:     
        def mw(s):
            dt,ds={c:t.count(c) for c in set(list(t))},{}
            ltc=set(dt.keys())
            left,right=0,0
            tli,minli=[],[0,0] #[left,right)
            #i = left
            #while i<len(s):
            for i in range(left,len(s)):
                c = s[i]
                ds[c]= ds.get(c,0)+1
                if c in ltc and ds[c]>=dt[c]:  ltc.remove(c)
                if not ltc :
                    tli.append((left,i+1))
                    #print('empty ltc',s[left:i+1],tli)
                    if minli==[0,0] or i+1-left<minli[1]-minli[0] : minli=[left,i+1]
                    j = left
                    while j<i+1:
                        cc =s[j]
                        ds[cc]-=1
                        if cc in dt and ds[cc]<dt[cc]:
                            tli.append((j,i+1))
                            if i+1-j <minli[1]-minli[0]:  minli=[j,i+1]
                            #print(tli,s[j:i+1],'add %s'%cc)
                            ltc.add(cc)
                            break
                        j+=1
                    left =j+1
                #i+=1
            print(tli,minli,i-left)
            return minli

        left,right   =  mw(s)
        return s[left:right] if right>0 else ''