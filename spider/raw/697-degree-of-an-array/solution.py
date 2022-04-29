class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dn={}
        for i in range(len(nums)):
            n = nums[i]
            dn.setdefault(n,[0,i,i])
            dn[n][0]+=1
            dn[n][2]=i
        srt = sorted(dn.items(),key=lambda xx:xx[1][0]*10000+(xx[1][1]-xx[1][2]),reverse=True)
        print(srt)

        return srt[0][1][-1]-srt[0][1][-2]+1