class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(tup):
            srt = sorted(tup,key=lambda xx:xx[0])
            return sum([1 if (srt[i][0]== srt[i-1][0] and srt[i][1]!= srt[i-1][1]) or (srt[i][0]!= srt[i-1][0] and srt[i][1]== srt[i-1][1]) else 0 for i in range(1,len(srt))])==0
        return len(list(s))==len(list(t)) and check(zip(list(s),list(t))) and check(zip(list(t),list(s)))        