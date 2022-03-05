class DetectSquares:

    def __init__(self):
        self.pdic = {}
        self.xnum ={}
        self.ynum={}

    def add(self, point: List[int]) -> None:
        x,y = point
        self.pdic.setdefault((x,y),0) 
        self.pdic[(x,y)]+=1
        self.xnum.setdefault(x,{})
        self.xnum[x].setdefault(y,0)
        self.xnum[x][y]+=1
        self.ynum.setdefault(y,{})
        self.ynum[y].setdefault(x,0)   
        self.ynum[y][x]+=1         

    def count(self, point: List[int]) -> int:
        x,y = point
        p4ys = self.xnum.get(x,{})
        p2xs = self.ynum.get(y,{})
        cnt = 0

        for p1x in p2xs:
            if p1x==x:continue
            for p1y in p4ys:
                if p1y==y:continue
                if abs(p1x-x) != abs(p1y-y) :continue
                if (p1x,p1y) in self.pdic:
                    cnt += self.pdic[(p1x,p1y)]*p2xs[p1x]*p4ys[p1y] if (p1x,p1y) in self.pdic else 0
        #print(point,p2xs,p4ys,cnt)
        return cnt
            




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)