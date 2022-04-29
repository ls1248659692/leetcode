class Solution:
    def wordPattern(self, pat: str, strg: str) -> bool:
        # def check(tup):
        #     s = sorted(tup)
        #     return sum([(s[i][0]== s[i-1][0] and s[i][1]!= s[i-1][1]) or (s[i][0]!= s[i-1][0] and s[i][1]== s[i-1][1]) for i in range(1,len(s))])==0
        # return len(list(pat)) == len(strg.split()) and check(zip(list(pat), strg.split())) and check(zip(strg.split(), list(pat)))

        p,s=list(pat),strg.split()
        return [dict(zip(p,s)).get(pp,None) for pp in p]==s and [dict(zip(s,p)).get(ss,None) for ss in s]==p