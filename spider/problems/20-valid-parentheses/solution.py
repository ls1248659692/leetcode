class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s=s.replace('()','').replace('[]','').replace('{}','')
        return True if s=='' else False
        
        t = ''
        for c in s:
            if c in '({[':t+=c
            else:
                if not t: return False
                elif  t[-1]!={']':'[',')':'(','}':'{'}[c]:return False
                else: t = t[:-1]
        return True if t=='' else False