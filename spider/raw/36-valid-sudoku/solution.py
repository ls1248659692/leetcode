class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        g=board
        for r in g:
            ct = Counter([e for e in r if e!='.']).most_common()
            if ct and ct[0][1]>1:return False
        for j in range(9):
            ct =Counter([g[i][j] for i in range(9) if g[i][j]!='.']).most_common()
            if ct and ct[0][1]>1:return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                ct=Counter([g[i+m][j+n] for m in range(3) for n in range(3) if g[i+m][j+n]!='.']).most_common()
                if ct and ct[0][1]>1:return False
        return True