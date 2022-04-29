class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def bs(s):
            nli=[]
            for c in s:
                if c=='#':
                    if nli:nli.pop()
                else: 
                    nli.append(c)
            print (''.join(nli))
            return ''.join(nli)
        return bs(s)==bs(t)