class Solution:
    def strToInt(self, str: str) -> int:
        s = str
        pstr = s
        pstr=pstr.strip()
        print(','+pstr)
        negpos = 1
        maxp = '2147483647' #str(2**31-1) 
        maxn= '2147483648'  #str(2**31)
        if not pstr:return 0
        if pstr[0] not in '+-0123456789':return 0
        while pstr[0] not in '+-0123456789': pstr = pstr[1:]
        
        if pstr[0] in '+-': 
            negpos = -1 if pstr[0]== '-' else 1
            pstr= pstr[1:]
        while pstr and pstr[0]  in '0': pstr = pstr[1:]
        if not pstr or pstr[0] not in '0123456789':return 0    
       
        t_pstr = pstr
        n_pstr = ''
        for cc in t_pstr:
            if cc in '0123456789':
                n_pstr += cc
            else:
                break
        pstr = n_pstr 

        if len(pstr)<10:
            return int(pstr)*negpos
        elif len(pstr)>10:
            return 2**31-1 if negpos>0 else -2**31
        else:
            if negpos>0 and pstr>=maxp: return  2**31-1
            if negpos<0 and pstr>=maxn: return -2**31
            return negpos * int(pstr)        