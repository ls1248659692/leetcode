class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        mxi = arr.index(max(arr))
        return mxi if sorted(arr[:mxi])==arr[:mxi] and  sorted(arr[mxi:],reverse=True)==arr[mxi:] else -1        