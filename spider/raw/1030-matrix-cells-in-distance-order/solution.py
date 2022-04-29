class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        li = []
        for r in range(rows):
            for c in range(cols):
                li.append([r,c])
        li = sorted(li,key = lambda x:abs(x[0]-rCenter)+abs(x[1]-cCenter))
        return li

        
        