class Solution:
    def tictactoe(self, m: List[List[int]]) -> str:
        def v1(m):
            seta = set(['%s%s'%(e[0],e[1]) for i,e in enumerate(m) if i%2==0])
            setb = set(['%s%s'%(e[0],e[1]) for i,e in enumerate(m) if i%2==1])
            for s in '00 11 22,02 11 20,00 01 02,10 11 12,20 21 22,00 10 20,01 11 21,02 12 22'.split(','):
                if set(s.split()).issubset(seta): return "A"
                if set(s.split()).issubset(setb): return "B"
            return "Draw" if len(m)==9 else 'Pending'

        def v2(m):
            onel=lambda s,rc:max([sum(e[rc]==str(i) for e in s) for i in range(3)])==3  
            crs=lambda s:set(['00','11','22']).issubset(s) or  set(['02','11','20']).issubset(s) 
            seta = set(['%s%s'%(e[0],e[1]) for i,e in enumerate(m) if i%2==0])
            setb = set(['%s%s'%(e[0],e[1]) for i,e in enumerate(m) if i%2==1])    
            if  onel(seta,0) or onel(seta,1) or crs(seta):return "A"    
            if  onel(setb,0) or onel(setb,1) or crs(setb):return "B"    
            return "Draw" if len(m)==9 else 'Pending'

        def v3(m):
            onel=lambda s,rc:max([sum(e[rc]==i for e in s) for i in range(3)])==3
            crs=lambda s:set([(i,i)for i in range(3)]).issubset(s) or  set([(i,2-i) for i in range(3)]).issubset(s) 
            seta = set([tuple(e) for i,e in enumerate(m) if i%2==0])
            setb = set([tuple(e) for i,e in enumerate(m) if i%2==1])
            if  onel(seta,0) or onel(seta,1) or crs(seta):return "A"    
            if  onel(setb,0) or onel(setb,1) or crs(setb):return "B"    
            return "Draw" if len(m)==9 else 'Pending'            
        return v3(m)