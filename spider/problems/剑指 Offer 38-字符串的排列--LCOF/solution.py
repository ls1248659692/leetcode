class Solution:
    def perm_k(self,pstr):
        res = ['']
        if  pstr:
            for ii in range(len(pstr)):
                res += [pstr[ii]+ el for el in self.perm_k(pstr[:ii]+pstr[ii+1:])]
        return res

    def permutation(self, s: str) -> List[str]:
        res =self.perm_k(s)
        return list(set([el for el in res if len(el)==len(s)]))