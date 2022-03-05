class Solution:
    def replaceDigits(self, s: str) -> str:
        return ''.join([ chr(ord(s[ii-1])+int(s[ii])) if ii%2==1 else s[ii] for ii in range(len(s))])