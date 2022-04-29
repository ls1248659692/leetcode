class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        px,py=0,0
        obset = set([tuple(p) for p in obstacles])
        while not(px==x and py==y):
            for c in command:
                 if c=='R': px+=1
                 else: py+=1
                 if px==x and py==y:return True
                 if px>x or py>y:return False
                 if (px,py) in obset: return False
        return True