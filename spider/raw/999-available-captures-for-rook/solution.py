class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        b =board
        R=[(i,b[i].index('R')) for i in range(len(b)) if 'R' in b[i]][0]
        print(R)
        x,y,cnt=R[0],R[1],0
        rgs = [range(x,8),range(x-1,-1,-1),range(y,8),range(y-1,-1,-1)]
        for r in range(len(rgs)):
            for i in rgs[r]:
                c = b[i][y] if r<2 else b[x][i]
                if c=='B':break
                if c=='p':
                    cnt+=1
                    break
        return cnt