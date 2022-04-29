class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        f,s = (first,second) if len(first)>len(second) else (second,first)
        edn=lambda a,b,n:sum(0 if a[i]==b[i] or b[i]=='.'  else 1 for i in range(len(a)) )<=n
        print(f,s)
        if len(f)==len(s):
            return edn(f,s,1)
        elif len(f)==len(s)+1:
            if len(s)==0: return edn(f,'.',0)
            for i in range(len(s)+1):
                t=s[:i]+'.'+s[i:]
                print(f,t)
                if edn(f,t,0):
                    print(f,t,0)
                    return True
            return False
        return False