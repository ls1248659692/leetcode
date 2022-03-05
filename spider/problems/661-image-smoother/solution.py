class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [ [] for i in range(len(img))]
        marginx = len(img)
        marginy = len(img[0])
        for i in range(len(img)):
            img[i].insert(0,None)
            img[i].append(None)
        img.insert(0,[None]*(marginy+2))
        img.insert(len(img),[None]*(marginy+2))
        for x in range(1,1+marginx):
            for y in range(1,1+marginy):
                surrouding_list = [img[x-1][y-1],img[x-1][y],img[x-1][y+1],img[x][y-1],img[x][y],img[x][y+1],img[x+1][y-1],img[x+1][y],img[x+1][y+1]]
                surrouding_list = [x for x in surrouding_list if x is not None]
                val_get= (sum(surrouding_list)//len(surrouding_list))
                ans[x-1].append(val_get)
        return ans