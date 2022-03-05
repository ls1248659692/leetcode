class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        r=[s[0].lower(),s[0].upper()] if s[0].isalpha() else [s[0]]
        for i in range(1,len(s)):
            r= [e+s[i].upper() for e in r] +([e+s[i].lower() for e in r]  if s[i].isalpha()else [])
        return r