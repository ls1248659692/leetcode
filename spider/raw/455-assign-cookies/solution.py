class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g =sorted(g)
        s = sorted(s)
        m =0
        while g and s:
            while g and s[-1]<g[-1]:
                #print('g.pop',s,g)
                g.pop()
            else:
                #print(g,s)
                if g:
                    s.pop()
                    g.pop()
                    m+=1
        return m