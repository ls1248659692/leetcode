class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums in [[0],[1]]:return 0
        aset,tset,nu,ln,cnt =set([i for i in range(nums[0]+1)]),set([i for i in range(nums[0]+1)]),nums,len(nums),1
        if ln-1 in tset:return cnt
        while aset:
            #print(cnt,aset,tset)
            cnt+=1
            _aset,aset=set(aset),set()
            for i in _aset:
                for j in range(i-nu[i],i+nu[i]+1):
                    if j>=ln: return cnt
                    if j>=0 and j not in tset: aset.add(j)
            for i in aset:tset.add(i)
            if ln-1 in tset:return cnt
        return 0
        