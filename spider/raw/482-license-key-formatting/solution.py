class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace('-','').upper()
        s= ' '*((len(s)//k+1)*k-len(s)) + s 
        r= '-'.join([s[i*k:(i+1)*k].strip() for i in range(len(s)//k) if s[i*k:(i+1)*k].strip()])
        return r