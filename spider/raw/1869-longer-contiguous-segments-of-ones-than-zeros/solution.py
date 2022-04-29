class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s= 'a'+s+'z'
        tli =[[s[ii-1],ii] for ii in range(1,len(s)) if s[ii-1]!=s[ii]]
        t2li = [tli[ii]+[tli[ii][-1]-(tli[ii-1][-1] if ii>0 else 0)] for ii in range(len(tli))]
        print(tli,t2li)
        if not t2li:return False
        return max([t[-1]if t[0]=='1' else 0 for t in t2li ])>max([t[-1] if t[0]=='0' else 0 for t in t2li ])