class Solution:
    def sortString(self, s: str) -> str:
        # sli = sorted([c*s.count(c) for c in set(s)],key=lambda xx:len(xx),reverse=True)
        # return ''.join([''.join(sorted(''.join([ss[ii:ii+1] for ss in sli]),reverse=ii%2))  for ii in range(len(sli[0]))])

        r,d = '',{c:s.count(c) for c in set(s)}
        while d:
            r,d= r+''.join(sorted(list(d.keys()))), {c:d[c]-1 for c in d if d[c]>1}
            r,d= r+''.join(sorted(list(d.keys()),reverse=True)),{c:d[c]-1 for c in d if d[c]>1}       
        return r