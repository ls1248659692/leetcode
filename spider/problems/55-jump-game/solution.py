class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums: return True
        if nums ==[0]:return True
        nli= []
        maxn=0
        for ii  in range(len(nums)):
            if maxn<nums[ii]+ii:maxn=nums[ii]+ii
            nli.append([ii,nums[ii],nums[ii]+ii,maxn]) 
        print(nli)
        nxt= 0
        while  nxt<len(nli) and nli[nxt][-1]>nxt:
            nxt=nli[nxt][-1]
        print(nxt)
        return nxt>=len(nli)-1
