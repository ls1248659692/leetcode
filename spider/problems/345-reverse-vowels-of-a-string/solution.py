class Solution:
    def reverseVowels(self, s: str) -> str:
        sli = list(s)
        vli = [[i,s[i]] for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        vr = [el[-1] for el in vli]
        vr = vr[::-1]
        for v in range(len(vli)):
            sli[vli[v][0]]=vr[v]
        return ''.join(sli)