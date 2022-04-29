class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ele = []
        for x in grid:
            for y in x:
                ele.append(y)
        k = k % len(ele)
        ele = ele[-k:] + ele[:-k]
        print(ele)
        i = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                grid[a][b] = ele[i]
                i = i +1
        return(grid)