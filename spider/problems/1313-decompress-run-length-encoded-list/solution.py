class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        t = [[nums[i+1]]*nums[i]for i in range(0,len(nums),2)]
        #print(t)
        return [e for r in t for e in r]