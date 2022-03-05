class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # yma,ymi = max([p[1] for p in points if p[0]==0]),min([p[1] for p in points if p[0]==0])
        # xma,xmi = max([p[0] for p in points if p[1]==0]),min([p[0] for p in points if p[1]==0])
        # return max((yma-ymi)*xma/2,(xma-xmi)*yma/2)
        # area = 0 
        # for pointa in points:
        #     for pointb in points:
        #         for pointc in points:
        #             if pointa != pointb and pointb != pointc and pointc != pointa:
        #                 a = pointa[0]
        #                 b = pointb[0]
        #                 c = pointc[0]
        #                 x = pointa[1]
        #                 y = pointb[1]
        #                 z = pointc[1]
        #                 temp = (0.5*(a*(y-z) + b*(z-x) + c*(x-y)))
        #                 if temp > area :
        #                     area = temp

        # return area

                            
        def ar(a,b,c):
            x1,y1=a
            x2,y2=b
            x3,y3=c
            #print(x1,y1,x2,y2,x3,y3)
            return abs(0.5*(x1*(y2-y3)+ x2*(y3-y1)+ x3*(y1-y2)))      

        mxs=0
        # for i,a in enumerate(points):
        #     for j,b in enumerate(points):
        #         if j<=i:continue
        #         for k,c in enumerate(points):
        #             if k<=j:continue
        ln= len(points)
        for i in range(ln):
            for j in range(i+1,ln):
                for k in range(j+1,ln):
                    sq=ar(points[i],points[j],points[k])   
                    #print(points[i],points[j],points[k],sq)

                    if mxs<sq:mxs=sq
        return mxs