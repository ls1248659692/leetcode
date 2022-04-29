class Solution:
    def convert(self, s: str, numRows: int) -> str:    
        nr = numRows
        unitss= numRows*2-2
        if nr==1:return s
        elif nr==2: return ''.join([s[ii] for ii in range(len(s)) if ii%2==0]) +''.join([s[ii] for ii in range(len(s)) if ii%2==1])
        elif nr==3:
            tli = []
            for r in range(nr): #4
                if r==0:tli.append([s[ii] for ii in range(len(s)) if ii%unitss==0])  
                if r==1:tli.append([s[ii] for ii in range(len(s)) if ii%unitss in [1,unitss-1]])
                if r==2:tli.append([s[ii] for ii in range(len(s)) if ii%unitss in [2]])
            return  ''.join([''.join(sub) for sub in tli])
        elif nr>=4:
            tli = []
            for r in range(nr):#6
                tli.append([s[ii] for ii in range(len(s)) if ii%unitss in [r,unitss-r]])
            return  ''.join([''.join(sub) for sub in tli])

    def convert_v1(self, s: str, numRows: int) -> str:
        if numRows==1:return s
        unitsc = numRows-1
        unitss= numRows*2-2
        li = [' ']*((int(len(s)/unitss)+1)*unitsc)
        mli = [list(li) for ii in range(numRows)]
        numCols = len(mli[0])
        pstr = s + '-'*(numRows*numCols-len(s))
        for cc in range(numCols):
            for rr in range(numRows):
                if cc%unitsc==0 and int(cc/unitsc)*unitss+rr<len(pstr):
                    mli[rr][cc]=pstr[int(cc/unitsc)*unitss+rr]
                elif rr==unitsc-cc%unitsc and int(cc/unitsc)*unitss+unitss+-rr<len(pstr):
                    mli[rr][cc]=pstr[int(cc/unitsc)*unitss+unitss-rr]
        nstr=''
        for rr in range(numRows):
            for cc in range(numCols):
                if mli[rr][cc]!=' ': nstr+= mli[rr][cc]
        return nstr.replace('-','')