class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        img= image
        iset,isetb =set([(sr,sc)]) ,set()
        while iset != isetb:
            isetb=set(iset)
            for r,c in isetb:
                for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                    if 0<=r+i<len(img) and 0<=c+j<len(img[0]) and img[r+i][c+j] ==image[sr][sc]: iset.add((r+i,c+j))

        for r in img: print(r)
        for r,c in isetb: image[r][c]=newColor
        return image    