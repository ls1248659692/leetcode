class Solution:
    def __init__(self):
        self.cache={}

    def permut(self,chars):
        if ''.join(sorted(chars)) in self.cache: return self.cache[''.join(sorted(chars))]
        if len(chars)==1:
            self.cache[''.join(chars)]=chars
            return chars
        else:
            rli = ['']*len(chars)
            for ii in range(len(chars)):
                rli[ii]= [chars[ii]+el for el in self.permut(chars[:ii]+chars[ii+1:])]
            pli=[]
            for rr in rli:
                pli.extend(rr)
            self.cache[''.join(sorted(chars))]=pli
            return pli

    def checkInclusion(self, s1: str, s2: str) -> bool:
        srt_s1 = sorted(list(s1))
        for ii in range(len(s2)-len(s1)+1):
            if sorted(list(s2[ii:ii+len(s1)]))==srt_s1: return True
        return False