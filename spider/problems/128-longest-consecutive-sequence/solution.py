class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sn = sorted(list(set(nums)))
        if not sn:return 0
        cmx = [[sn[0],sn[0]]]
        for n in sn[1:]:
            if n ==  cmx[-1][-1]+1: cmx[-1][-1]+=1
            else: cmx.append([n,n])
        print(cmx)
        return max([int(e[1]-e[0]+1) for e in cmx])