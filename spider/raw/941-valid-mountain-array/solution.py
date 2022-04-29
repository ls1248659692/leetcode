class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        singled = lambda  x:   False if [ i for i in range(1,len(x)) if (x[i]-x[i-1])*(x[1]-x[0])<=0] else True
        mxi = arr.index(max(arr))
        return singled(arr[:mxi]) and singled(arr[mxi:]) and mxi not in [0,len(arr)-1]