class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # a = points[0][0]
        # b = points[1][0]
        # c = points[2][0]
        # x = points[0][1]
        # y = points[1][1]
        # z = points[2][1]
        # return True if (0.5*(a*(y-z) + b*(z-x) + c*(x-y))) != 0 else False

        s= sorted(points)
        #if s[0][0]==s[1][0]==s[2][0]: return False
        return (s[1][1]-s[0][1])  * (s[2][0]-s[0][0])!=  (s[2][1]-s[0][1]) *(s[1][0]-s[0][0])        