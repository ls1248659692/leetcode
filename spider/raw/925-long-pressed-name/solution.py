class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def v1(name,typed):
            def dsplit(s):
                rli =[s[0]]
                for c in s[1:]:
                    if c!=rli[-1][-1]:rli.append(c)
                    else:rli[-1] +=c
                return rli

            nli = dsplit(name)
            tli = dsplit(typed)
            if len(nli)!=len(tli):return False
            for i in range(len(nli)):
                if nli[i][0]!=tli[i][0] :return False
                if len(nli[i])>len(tli[i]):return False
            return True

        def v1b(name,typed):
            def firstc(s,c):
                for i in range(len(s)+1):
                    if i==len(s) or s[i]!=c:break
                return s[i:],i    

            while len(name)>=1:
                print(name,typed)
                n0= name[0]
                name,i = firstc(name,n0)
                if typed[:i]!=n0*i: return False
                typed,_i=firstc(typed,n0)   
            return False if typed else True

        return v1b(name,typed)