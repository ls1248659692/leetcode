class Solution:
    def findRadius(self, ho: List[int], ha: List[int]) -> int:
        ho,ha,mir = sorted(ho),[float('-inf')]+sorted(ha),0
        while len(ha)>1 and ha[-2]>ho[-1]:ha.pop()
        while ho and len(ha)>1:
            #print('.',mir,ho,ha)

            mi=min(abs(ho[-1]-ha[-1]),abs(ho[-1]-ha[-2]))
            if mir<mi: mir = mi

            ho.pop()
      
            while ho and len(ha)>1 and ho[-1]<ha[-2]:
                ha.pop()

        
        print(mir,ho,ha)
        #if len(ha)==1: mir = max(mir,max(abs(o-ha[0]) for o in ho))
        return mir