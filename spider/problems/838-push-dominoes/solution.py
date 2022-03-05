def dsplit(s):
    r = [s[0]]
    for c in s[1:]:
        if ('R' in c and 'L' in r[-1]) or ('L' in c and 'R' in r[-1]):
            r.append('')
        r[-1] += c
    return r

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def tcalc(s):
            suf =  len(s)-len(s.rstrip('.'))
            return s[:len(s)-suf].replace('.',s[0])+s[len(s)-suf:]    

        def pdom(s):            
            rls =[tcalc(s) for s in dsplit(s)]
            for i in range(0,len(rls)-1):
                s= rls[i]
                if s[0]=='R':
                    suf =  len(s)-len(s.rstrip('.'))
                    rls[i]=s[:len(s)-suf]+'R'*(suf//2) +('.' if suf%2 else '') +'L'*(suf//2)
            return ''.join(rls)

        if set(list(dominoes))==set(['.']):return dominoes
        dd= dominoes.lstrip('.')
        d = dd.rstrip('.')
        return  ('L' if dd[0]=='L' else '.')*(len(dominoes)-len(dd))+ pdom(d) + ('R' if d[-1]=='R' else '.')*(len(dd)-len(d))